from mac.gui import collect_info, show_results
from mac.logic import run_suite


def main():
    agents, num_of_iterations = collect_info()

    agents, graph_data = run_suite(agents, num_of_iterations)

    show_results(graph_data)


if __name__ == "__main__":
    main()