Supplementary Material to: A Game-Theoretic Approach for Optimal Multi-Target Defense Strategies in Programmable Networking
===

### Jamil Ahmad Kassem, Internet Interdisciplinary Institute (IN3) and Universitat Oberta de Catalunya (UOC)
### Helena Rifà-Pous, Internet Interdisciplinary Institute (IN3) and Universitat Oberta de Catalunya (UOC)
### Joaquin Garcia-Alfaro, SAMOVAR, Institut Polytechnique de Paris, Telecom SudParis, 91120 Palaiseau, France

## Abstract

Traditional network defense strategies, which follow a linear sequence of vulnerability discovery, defense selection, and attack mitigation, often struggle to adapt to emerging and unpredictable cyber threats. This paper introduces a novel strategic framework designed to optimize defense costs that addresses security concerns and cost-effectiveness. Drawing inspiration from Bayesian Stackelberg game theory, our approach introduces a novel resource management strategy. We test our approach over the programmable networking paradigm, which is already expected to expand traditional network architectures to ease the management of new properties, including the incorporation of new security functionality. We conduct experimental work assuming a representative setup over Software Defined Networking protocols. We show that our solution outperforms existing methods by reducing defense costs and offering defenders the flexibility to minimize the attack's impact or the overall cost. Our work establishes a foundation for developing advanced models with more detailed representations of system resources.

*Keywords:* Cyberdefense, Programmable Network, Software Defined Networking, Moving Target Defense, Game Theory.

*Version:* May 27, 2025

## Reference

If using this code for research purposes, please cite:

J. A. Kassem, H. Rifà-Pous, J. Garcia-Alfaro. A Game-Theoretic Approach for Optimal Multi-Target Defense Strategies in Programmable Networking. *Under review*, 2025.

```
@inproceedings{kassem2025optimal,
  title={{A Game-Theoretic Approach for Optimal Multi-Target Defense Strategies in Programmable Networking}},
  author={Kassem, Jamil Ahmad and Rifà-Pous, Helena and Garcia-Alfaro, Joaquin},
  booktitle={},
  pages={},
  year={2025},
  organization={},
  doi={},
  url={},
}
```

````markdown
# Path Switching Network Simulation with Ryu Controller

This repository contains the source code and tools for simulating a **path-switching network** governed by a custom **Ryu SDN controller**. The system is designed based on a matrix formulation described in our accompanying [scientific paper](#), and includes both attack simulation and network visualization.

---

## 🧠 Overview

The system creates a dynamic SDN-based network composed of `m` hosts and `n` paths, using a custom controller that reacts to simulated attacks and switches paths accordingly. The behavior of the system is governed by a matrix `A`, which determines connectivity and attack dynamics as presented in our publication.

---

## 📄 Associated Paper

> 📘 *[Insert Paper Title Here]*  
> *[Author Names], [Affiliation], [Conference/Journal Name]*  
> [[DOI or arXiv link]](#)

---

## 📁 Project Structure

```text
.
├── main.py                  # Main script to initialize, run and simulate the network
├── ryu_controller_basic.py # Custom Ryu controller used to control switch behavior
├── visualize_network.py    # Generates an HTML visualization of the network topology
├── plotter.py              # Plots network traffic after simulation
├── tmp_flow.txt            # Temporary file used to store traffic logs (auto-generated)
````

---

## ⚙️ System Description

1. **Network Creation**

   * The simulation starts by defining an `A` matrix as described in our paper.
   * The matrix defines how hosts and switches are interconnected.
   * One host is assigned as the attacker and another as the target.

2. **Controller Operation**

   * The Ryu controller reads link topology and installs flow rules.
   * It is started using:

     ```bash
     sudo ryu-manager --observe-links ryu_controller_basic.py
     ```

3. **Visualization**

   * The network is visualized using `visualize_network.py`, which uses `pyvis` to generate a standalone HTML file.

4. **Traffic Monitoring**

   * Traffic is monitored using `bwm-ng`, and stored in a temporary file (`tmp.txt`).
   * This file is later parsed and plotted using `plotter.py`.

5. **Attack Simulation**

   * A DDoS-style attack is simulated using `hping3` from the attacker to the target.
   * Attack duration is 5 seconds, followed by 10 seconds of post-attack monitoring.

6. **Shutdown**

   * All monitoring and network components are gracefully stopped.
   * Final traffic plots are generated.

---

## ▶️ How to Run

1. **Start the Controller**

   ```bash
   sudo ryu-manager --observe-links ryu_controller_basic.py
   ```

2. **Run the Simulation**
   In a new terminal:

   ```bash
   sudo python3 main.py
   ```

---

## 🛠 Requirements

* Python 3.x
* [Ryu SDN Framework](https://osrg.github.io/ryu/)
* `bwm-ng`, `hping3`
* Python packages:

  * `pyvis`
  * `matplotlib`
  * `networkx`

Install dependencies (Ubuntu example):

```bash
sudo apt install bwm-ng hping3
pip install pyvis matplotlib networkx
```

---

## 📊 Output

* `topology.html`: Network topology in interactive format
* `tmp.txt`: Intermediate data for bandwidth usage

---

## 📬 Contact

For questions or collaborations, please reach out to \[[jahmadkassem@uoc.edu](mailto:jahmadkassem@uoc.edu)].

```

## License

This project is licensed under the MIT License.



