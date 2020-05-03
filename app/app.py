"""
Determine if business considered active based on occurrences in the events.

__author__ = 'Max Luckystar'
__email__ = 'max.datascience@gmail.com'
__website__ = 'https://www.linkedin.com/in/bigdatamax/'
__ copyright__ = 'Copyright 2020, Max Luckystar' __version__ = '1.0'
"""

import csv
import json
from functools import singledispatch
import sys


class Order:
    """Order class."""

    def __init__(self, id, name, dependencies=[]):
        """Create object instance.

        Arguments:
            id {[number]} -- [order id number 0..10,000]
            name {[string]} -- [order name 1..100 character]

        Keyword Arguments:
            dependencies {list} -- [list of order objects] (default: {[]})
        """
        self.id = id
        self.name = name
        self.dependencies = dependencies

    def __repr__(self):
        """Class representation.

        Returns:
            [string] -- [string representation of the object]
        """
        return f'Order id = "{self.id}" name = "{self.name}" dependencies ="{self.dependencies}"'

    def toJSON(self):
        """Convert class to JSON.

        Returns:
            [type] -- [description]
        """
        return {
            'id':  self.id,
            'name': self.name,
            'dependencies': self.dependencies
        }


@singledispatch
def json_fomat(arg):
    try:
        return arg.toJSON()
    except AttributeError:
        return vars(arg)
    except TypeError:
        return str(arg)


def main(argv):
    """Run main module.

    Arguments:
        argv {[string]} -- [Command line arguments]
    """
    path_to_orders_file = argv[0]
    path_to_dependencies_file = argv[1]
    path_to_output_file = argv[2]
    orders_out = {}
    dependent_orders = []

    # create dictionary from order file
    with open(path_to_orders_file, 'r') as f_ord:
        orders = csv.reader(f_ord)
        next(orders)

        for order in orders:
            # ex. ['1', 'Pick up pipes and tiles']
            order_id = int(order[0].strip())
            if order_id in range(10000):
                orders_out[order_id] = Order(order_id, order[1])

    # add dictionary with dependencies of orders
    with open(path_to_dependencies_file, 'r') as f_dep:
        depend = csv.reader(f_dep)
        next(depend)
        for dep_order in depend:
            # key of order to complete first
            pred_key = int(dep_order[0].strip())

            # key of current order
            key = int(dep_order[1].strip())
            dependent_orders.append(key)

            # link to current order
            link = orders_out[key]
            dep_list = orders_out[pred_key].dependencies.copy()
            dep_list.append(link)
            orders_out[pred_key].dependencies = dep_list

    # prepare for output to json
    list_n = {'orders': []}
    for key, value in orders_out.items():
        if key not in dependent_orders:
            list_n['orders'].append(value)

    # output dictionary to json
    with open(path_to_output_file, 'w') as f_json:
        json.dump(list_n, f_json, indent=2, default=json_fomat)


if __name__ == "__main__":
    main(sys.argv[1:])
