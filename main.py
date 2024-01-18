from mac.gui import collect_info, show_graph_results, show_table_results
from mac.logic import run_suite, anti_cheat_eval


def main():
    agents, num_of_iterations = collect_info()

    agents, graph_data, statistic_data, agent_distribution = run_suite(
        agents, num_of_iterations
    )

    anti_cheat_eval(
        num_of_iterations=num_of_iterations,
        agent_list=agent_distribution,
    )

    show_graph_results(result=graph_data, statistic_data=statistic_data)
    # show_table_results()


if __name__ == "__main__":
    main()
