from api import get_friends


def get_network(users_ids, as_edgelist=True):
    vertices = ['me']
    edges = []
    ids = []
    cipher = {}
    for user_id in users_ids['response']['items']:
        name = user_id['first_name'] + user_id['last_name']
        user_id = user_id['id']
        ids.append(user_id)
        cipher.update({user_id : len(cipher.keys()) + 1})
        vertices.append(name)
    for user_id in users_ids['response']['items']:
        user_id = user_id['id']
        edges.append((0, cipher[user_id]))
        friends = get_friends(user_id, 'sex')
        try:
            for friend in friends['response']['items']:
                lable = friend['id']


                if lable in ids:

                    edges.append((cipher[user_id], cipher[lable]))

        except:
            pass
    if as_edgelist:
        print(edges)
    else:
        n = max(max(i, j) for i, j in edges)
        matrix = np.zeros((n, n))
        for i, j in edges:
            matrix[i-1][j-1] = 1
        for row in matrix:
            print(row)
    g = Graph(vertex_attrs={"label":vertices},
            edges=edges, directed=False)
    N = len(vertices)
    visual_style = {}
    visual_style["layout"] = g.layout_fruchterman_reingold(
    maxiter=1000,
    area=N**3,
    repulserad=N**3)
    g.simplify(multiple=True, loops=True)
    plot_graph(g, visual_style)


def plot_graph(graph):
    communities = g.community_edge_betweenness(directed=False)
    clusters = communities.as_clustering()
    print(clusters)
    pal = igraph.drawing.colors.ClusterColoringPalette(len(clusters))
    g.vs['color'] = pal.get_many(clusters.membership)
    plot(g, **visual_style)
    
  if __name__ == '__main__':
    get_network(get_friends(user_id, 'sex'), True