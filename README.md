# DPG SKM 2025 Tutorial: AI Fundamentals for Research (joint session BP/TUT/DY/AKPIK)

Sunday, 16th March 2025, 16:00–18:15, H2<br>
Presented at the **[2025 DPG Spring Meeting of the Condensed Matter Section](https://www.dpg-verhandlungen.de/year/2025/conference/regensburg/part/tut/session/1)**

### Abstract
 Artificial intelligence (AI) has become an essential tool in modern physics, enabling new approaches to data analysis, modeling, and prediction. This hands-on tutorial provides an accessible introduction to key AI concepts, emphasizing their practical applications in physics research.

Materials in this repository are also downloadable by clicking [this link.](https://jlubox.uni-giessen.de/getlink/fiAGRzcGTiCL3GZxk8WAjom4/)

Participants are encouraged to download the contents of this repository ahead of time.

### Organised by
Jan Bürger<sup>1</sup>, Janine Graser<sup>2</sup>, Robin Msiska<sup>2,3</sup>, and Arash Rahimi-Iman<sup>4</sup> with support from Stefan Klumpp<sup>5</sup> and Tim Ruhe<sup>6</sup>

<sup>1</sup>ErUM-Data-Hub, RWTH Aachen University, Aachen, Germany<br>
<sup>2</sup>Faculty of Physics and Center for Nanointegration Duisburg-Essen (CENIDE), University of Duisburg-Essen, Duisburg, Germany<br>
<sup>3</sup>Department of Solid State Sciences, Ghent University, Ghent, Belgium<br>
<sup>4</sup>I. Physikalisches Institut and Center for Materials Research, Justus-Liebig-University Gießen, Gießen, Germany<br>
<sup>5</sup>Institute for the Dynamics of Complex Systems , Universität Göttingen, Göttingen, Germany<br>
<sup>6</sup>Faculty of Physics, TU Dortmund University, Dortmund, Germany

## Getting Started on Your Own Device
If you have not yet downloaded this repository, you can do so in two ways. 
1. If you have `git` installed on your device, you can use the command:
    ```bash
    git clone https://github.com/RedMechanism/DPG-SKM-2025-Tutorial-AI-Fundamentals-for-Research.git
    ```
2. If you do not have `git`, go to the main page of the GitHub repository, click the green button labelled "Code" close to the top of the page, and then select `Download ZIP`. Unzip the archive.

    Alternatively, you can download this archive by clicking [this external link.](https://jlubox.uni-giessen.de/getlink/fiAGRzcGTiCL3GZxk8WAjom4/)


After downloading the repository, navigate to its folder (which contains the `requirements.txt` file). Then, create and activate a Python virtual environment. Once the environment is active, install the necessary dependencies by running:

```bash
pip install -r requirements.txt
```

If you're unsure how to create or activate a virtual environment, please refer to the [instructions here](creating_environment.md).

Finally, test your setup by running the `pyteser.py` script within the activated environment. Using the command
```bash
python pyteser.py
```
or
```bash
python3 pyteser.py
```
#### Start the Jupyter Notebook
To start Jupyter Notebook, run the following command in your terminal or command prompt
```bash
jupyter notebook
```
The command will automatically open a new tab in your default web browser with the Jupyter Notebook interface. If it doesn't, you can manually navigate to the URL provided in the terminal (usually http://localhost:8888).

If you are having trouble running the cells, it could be that your created virtual environment is not used by the Jupyter notebook. Click [this link](creating_environment.md#Installing-and-Running-the-IPython-venv-Kernel) for instructions on how to resolve this.

## Using the Online Notebooks
If you're unable to set up a working environment on your own machine, you may opt to use an online environment for Jupyter Notebooks. To do so, simply click on the JupyterHub badge below.

[![Binder](https://img.shields.io/badge/JupyterHub-Ready-orange?logo=jupyter)](https://plg.physlab.uni-due.de:80/hub/login?next=%2Fhub%2F)

***Note: Access details for this online environment will be provided during the session.***