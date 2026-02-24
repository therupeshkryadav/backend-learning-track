# main.py

from io_examples import run_io_demo
from string_examples import run_string_demo
from list_examples import run_list_demo
from tuple_examples import run_tuple_demo
from dict_examples import run_dict_demo
from set_examples import run_set_demo


def main():
    run_io_demo()
    run_string_demo()
    run_list_demo()
    run_tuple_demo()
    run_dict_demo()
    run_set_demo()


if __name__ == "__main__":
    main()