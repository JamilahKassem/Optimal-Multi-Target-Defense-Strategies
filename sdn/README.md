Supplementary Material to: A Game-Theoretic Approach for Optimal Multi-Target Defense Strategies in Programmable Networking
===

### Jamil Ahmad Kassem, Internet Interdisciplinary Institute (IN3) and Universitat Oberta de Catalunya (UOC)
### Helena Rifà-Pous, Internet Interdisciplinary Institute (IN3) and Universitat Oberta de Catalunya (UOC)
### Joaquin Garcia-Alfaro, SAMOVAR, Institut Polytechnique de Paris, Telecom SudParis, 91120 Palaiseau, France

## Abstract

Traditional network defense strategies, which follow a linear sequence of vulnerability discovery defense selection and attack mitigation, often struggle to adapt to emerging and unpredictable cyber threats. This paper introduces a novel strategic framework designed to optimize defense costs that addresses both security concerns and cost-effectiveness. Drawing inspiration from Bayesian Stackelberg game theory, our approach introduces a novel resource management strategy. Simulation results show that our solution outperforms existing methods by reducing defense costs and offering defenders the flexibility to minimize either the attack's impact or the overall cost. Our work establishes a foundation for developing advanced models with more detailed representations of system resources.

*Keywords:* Cyberdefense, Moving Target Defense, Game Theory, 
Logic Model, Cybersecurity.

*Version:* March 15, 2025

### Code

This MATLAB project implements a model designed to optimize costs associated with a moving target scenario. The code simulates various system configurations to analyze how performance metrics change when different parameters are adjusted. Specifically, the model considers resources (`m`), nodes (`n`), and the cost of movement (`cm`). The simulations compare the performance of three models: the baseline model, the Kassem model, and a newly introduced model.

## Project Structure

The project consists of main scripts that perform simulations by varying specific parameters and sub-scripts that support these simulations.

### Main Scripts

1. **compare_vary_cm.m**: Simulates and compares the costs of the three models while varying the cost of movement (`cm`).

2. **compare_vary_n.m**: Simulates and compares the costs of the three models while varying the number of nodes (`n`).

3. **compare_vary_m.m**: Simulates and compares the costs of the three models while varying the number of resources (`m`).

4. **minimize_cost_vs_impact.m**: Analyzes the trade-offs between optimizing total cost and optimizing the impact of cost variations.

### Sub-Scripts

1. **form_matrix.m**: Creates an `m x n` matrix representing the movement of resources within the system. The matrix elements are numbers ranging from 0 to 1.

2. **NumberofMoves.m**: Counts the number of moves for the new model introduced in the study.

3. **kassem_model.m**: Calculates the costs associated with the Kassem model.

4. **new_model.m**: Calculates the costs associated with the newly introduced model.

5. **base_model.m**: Calculates the costs associated with the baseline model.

## Usage

To utilize this project, run the main scripts in MATLAB. Each script will perform simulations based on the parameter it varies and generate plots illustrating the results. The plots are saved as SVG files in the current working directory.

**Example:**

To analyze how varying the number of nodes (`n`) affects the costs:

```matlab
compare_vary_n
```


This command will execute the `compare_vary_n.m` script, perform the simulations, and save the resulting plots.

## Requirements

- MATLAB (no additional toolboxes required)

## Reference

If using this code for research purposes, please cite:

J. A. Kassem, H. Rifà-Pous, J. Garcia-Alfaro. A Game-Theoretic Approach for Optimal Multi-Target Defense Strategies against Emerging Cyberattacks. *Under review*, 2025.

```
@inproceedings{kassem2025optimal,
  title={{A Game-Theoretic Approach for Optimal Multi-Target Defense Strategies against Emerging Cyberattacks}},
  author={Kassem, Jamil Ahmad and Rifà-Pous, Helena and Garcia-Alfaro, Joaquin},
  booktitle={},
  pages={},
  year={2025},
  organization={},
  doi={},
  url={},
}
```

## License

This project is licensed under the MIT License.

## Acknowledgments

This project structure and README template were inspired by the [MATLAB Project Template](https://github.com/reproducibleMATLAB/matlab-project-template). 
