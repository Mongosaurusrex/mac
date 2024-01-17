from mac.gui import collect_info, show_results
from mac.logic import run_suite


def main():
    agents, num_of_iterations = collect_info()

    agents, graph_data, statistic_data = run_suite(agents, num_of_iterations)

    show_results(result=graph_data, statistic_data=statistic_data)


if __name__ == "__main__":
    main()
