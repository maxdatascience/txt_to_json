# import os
import json
import csv
from pprint import pprint


# steps

def decode_dep(orders_out, key, value):
    # 1 ('Pick up pipes and tiles', [2, 3])
    # if len(value_list):
    #     # decode key -> id, name, list of dependencies
    #     key = str(value_list)
    #     name_dependencies = orders_out[value_list[0]]
    #     return  out = []
    for value in value_list:
        out = [str(key), value[0]]
        if len(value[1]):
            out.append[str(key), value[0]].append(
                decode_dep(orders_out, value[1]))
        else:
            out.append([])

        if length(value[1]):
            # include decode dependencies list
            out.append()
    else:
        # no dependencies
        out.append([])

    # try:
    #     art = getopt.getopt(
    #         # opts, args = getopt.getopt(
    #         argv[1:], "hi:o:", ["orders=", "dependencies=" "output="])
    #     print(art)
    # except getopt.GetoptError:
    #     print('app.py -i <orders> <dependencies> -o <outputfile>')
    #     sys.exit(2)
    # for opt, arg in opts:
    #     print(opt)
    #     print(arg)
    #     if opt == ("-h", "--help"):
    #         print('app.py -i <orders> <dependencies> -o <outputfile>')
    #         sys.exit()
    #     elif opt in ("-i", "--ifile"):
    #         path_to_orders_file = arg
    #         path_to_dependencies_file = arg2
    #     elif opt in ("-o", "--ofile"):
    #         path_to_output_file = arg
    #     else:
    #         assert False, "unrecognized option"


# def decode_dep(orders_out, value_list):
#     out = []
#     for value in value_list:

#         out.append(str(value), )

#         if length(value[1]):
#             # include decode dependencies list
#         out.append()
#     else:
#         # no dependencies
#         out.append([])


if __name__ == "__main__":
    p_ord = '/samba/alldev/github/venv/Hatchway/txt_to_json/data/orders.txt'
    p_depend = '/samba/alldev/github/venv/Hatchway/txt_to_json/data/dependencies.txt'
    p_out = '/samba/alldev/github/venv/Hatchway/txt_to_json/data/out_my.json'
    orders_out = {}

    # load all orders into dictionary with structure:
    # key: order id, value tuple: order name, empty list for dependencies
    # ex  1 ('Pick up pipes and tiles', [])
    orders = csv.reader(f_ord)
    next(orders)
    # print('\n')
    for order in orders:
            # print(order)
        key = int(order[0].strip())
        name = order[1].strip()
        orders_out[key] = (name, [])
    # print('\n\n')
    # print(orders_out)
    # print('\n\n')

    # define dependencies for each order filling the list of dependencies
    # ex. 1 ('Pick up pipes and tiles', [2, 3])
    with open(p_depend, 'r') as f_dep:
        depend = csv.reader(f_dep)
        next(depend)
        for dep_order in depend:
            # print(dep_order)
            key = int(dep_order[1].strip())
            dependon_key = int(dep_order[0].strip())
            orders_out[dependon_key][1].append(key)
    print(orders_out)

    # output dictionary to json

    print('\n\n')
    for key, value in orders_out.items():
        print(key, value)
        # decode the list of dependencies in value[1]
        # ex. 1 ('Pick up pipes and tiles', [2, 3]) it is list [2, 3]
        record = [str(key), value[0]].append(
            decode_dep(orders_out, key, value[1]))
        pprint(record)
