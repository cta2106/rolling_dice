from monte_carlo import MonteCarlo
import yaml

if __name__ == "__main__":

    config = yaml.safe_load(open("config.yml"))
    mc = MonteCarlo(config["n_iter"])
    mc.run_simulation()
    print("Second player advantage is: {:.4%}".format((mc.p2_win - mc.p1_win) / (mc.p1_win + mc.p2_win)))
