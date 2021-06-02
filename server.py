from flask import Flask, render_template, url_for
from table_to_graph import graph_dict
import operator

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
energy_dict1 = dict()


@app.route('/add_energy/<nama_node_str>')
def add_energy_to_nama_node(nama_node_str):
    energy_dict1['Nama-' + nama_node_str] = (
        energy_dict1.get('Nama-' + nama_node_str, 0) + 1)
    return energy_dict1

# @app.route('/reset')
# def reset_all_energy():
#     energy_dict1 = dict()


@app.route('/recomendation_product')
def generate_recommendation_from_current_energy_state():
    initial_nodes = []
    traversed_nodes = set()

    energy_dict = energy_dict1.copy()
    # Initial nodes
    for node in energy_dict:
        initial_nodes.append(node)

    bfs_queue = initial_nodes.copy()

    # Traverse each nodes
    while len(bfs_queue) > 0:
        current_node = bfs_queue.pop()
        if current_node in traversed_nodes:
            continue
        current_energy = energy_dict[current_node]

        adjacent_nodes = graph_dict[current_node]
        energy_to_be_shared = current_energy / len(adjacent_nodes)
        for node in adjacent_nodes:
            bfs_queue.append(node)
            energy_dict[node] = energy_dict.get(node, 0) + energy_to_be_shared

        traversed_nodes.add(current_node)

    recommendation_energy_dict = {}
    for node in energy_dict:
        if node in initial_nodes or not node.startswith('Nama-'):
            continue
        recommendation_energy_dict[node] = energy_dict[node]

    recommendation_list = sorted(
        recommendation_energy_dict.items(), key=operator.itemgetter(1),
        reverse=True)

    dict_recomendation_list = dict(recommendation_list)

    return dict_recomendation_list



@app.route('/')
def home():
    from table_to_graph import list_product


    return render_template('./index.html', product_name = list_product)

# with app.test_request_context():
#     print(url_for('add_energy_to_nama_node'))
    

if __name__ == "__main__":
    app.run(debug=True)