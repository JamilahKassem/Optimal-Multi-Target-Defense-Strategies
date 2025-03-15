# Moving Target Model Cost Optimization

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

## License

This project is licensed under the MIT License.

## Acknowledgments

This project structure and README template were inspired by the [MATLAB Project Template](https://github.com/reproducibleMATLAB/matlab-project-template). 
