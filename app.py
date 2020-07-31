# Imports
import os, flask, dash
from pathlib import Path
from random import randint
import dash_bootstrap_components as dbc

# Plots
from plotly.express import bar
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
from plotly import tools
import plotly.figure_factory as ff
from plotly.subplots import make_subplots 
    
   

# Import iPoster Object Class
from iposter.iposter import iPoster
import iposter.colors as colors

#*** Run Local Flag ***
RUN_LOCAL=False
# ******************Define Your Interactive Poster Here***************
# The following shows a sample interactive poster.
# Images for sections must be saved under the assets/ folder.
# You can import code from your own modules and construct the final dash
# interactive poster here.
def create_poster():

    # Instanitate an iPoster
    my_poster = iPoster(title="Research poster title; state the main topic of your study", # Title of your poster
                        authors_dict={"Eric Vazquez" : "University of Saint Mary", # Authors in {student, mentors, PI} order
                                      "Masakatsu Watanabe" : "Univeristy of Saint Mary",
                                      "Silvia Crivelli" : "Lawrence Berkeley National Laboratory"},
                        logo = "SM.png", # Home institution logo
                        banner_color=colors.DOE_GREEN, # Color of banner header; colors has preset colors
                        text_color=colors.WHITE)

    # Add sections to first column then add new column
    my_poster.add_section(title="Abstract",
                          text="Graphs are structures that are capable of representing the relationships between sets.\
                                Nodes are used to represent objects of these sets and the edges of the graph can show relations\
                                between these nodes. Using these properties graphical representations of proteins can be\
                                generated from information gathered from the Protein Data Bank (PDB).\
                                These protein graphs are beneficial for the analysis of proteins due to their ability to store  \
                                multiple features within both the nodes and edges of the graph.\
                                Several methods exist to compute the similarity between graphs. Using GraphDot, a GPU-\
                                accelerated Python library, a marginalized graph kernel based of the random walk\
                                paths is built to compute graph similarity. This package allows for the implementation \
                                of several node and edge features in the kernel process allowing for a spectrum \
                                of features to be analyzed.")
                          
    my_poster.add_section(title="Background Info",
                          text="Several biological pathways are determined by protein functionality. Understanding\
                                the way in which proteins control or regulate these pathways could lead to advances in medical\
                                treatments and therapies. A protein’s structure directly affects its functionality. Using a \
                                marginalized graph kernel, the connections between structure and functionality can be further \
                                explored by comparing the similarity of protein graph structures. ")
    my_poster.add_section(title="Marginalized Graph kernel", color=colors.LBNL_BLUE,
                          text="This method utilizes a Marginalized Graph Kernel to compute graph pairwise similarity. ",
                          img ={"filename":"Picture2.png", "height":"4.125in", "width":"11in", "caption":""}) 
                                      

    my_poster.next_column()

    # Add sections to second column then add new column
    
 
  
    fig = make_subplots(1, 3,
                       subplot_titles=("Secondary Structure", "Residue Type", "Secondary Structure & Residue Type"))
    
   
    fig.add_trace(go.Heatmap(
                   z=[[1.,0.80937215,0.81653635,0.68685985,0.8439209,0.85736667, 
               0.8085844, 0.83120887, 0.75444772, 0.55203045] ,
             [0.80937215, 1.,0.85558322, 0.72682671, 0.97925747, 0.81817356, 
              0.98876126, 0.86259989, 0.7346693,  0.63524418],
             [0.81653635, 0.85558322, 1.         ,0.70100128 ,0.86696107 ,0.84857677,
              0.84980589 ,0.98722697 ,0.67766673 ,0.51006481],
             [0.68685985, 0.72682671, 0.70100128, 1.         ,.75601048 ,0.62558967,
              0.73841499, 0.73212796 ,0.86533413 ,0.62848796],
             [0.8439209  ,0.97925747 ,0.86696107 ,0.75601048 ,1.         ,0.85632666,
              0.9815992 , 0.87043711 ,0.76438432 ,0.65863552],
             [0.85736667 ,0.81817356 ,0.84857677 ,0.62558967 ,0.85632666 ,1.,
              0.81249362 ,0.82127581 ,0.64156574 ,0.62807319],
             [0.8085844 , 0.98876126 ,0.84980589 ,0.73841499 ,0.9815992  ,0.81249362,
              1.        , 0.85805843 ,0.74430673 ,0.63574122],
             [0.83120887 ,0.86259989 ,0.98722697, 0.73212796, 0.87043711 ,0.82127581,
              0.85805843 ,1.         ,0.71339418 ,0.50124995],
             [0.75444772 ,0.73466923 ,0.67766673, 0.86533413 ,0.76438432 ,0.64156574,
              0.74430673, 0.71339418, 1.        , 0.6611413 ],
             [0.55203045, 0.63524418 ,0.51006481 ,0.62848796 ,0.65863552 ,0.62807319,
              0.63574122 ,0.50124995 ,0.6611413  ,1.        ]],
                   x=['1U07', '1IHR (A)', '2ABL', '1OPK (A)', '1QVC (A)','1QVC (B)','1PBG','1HZ6(A)','1OPK','2JWW'],
                   y=['1U07', '1IHR (A)', '2ABL', '1OPK (A)', '1QVC (A)','1QVC (B)','1PBG','1HZ6(A)','1OPK','2JWW'],
                   colorscale = 'Electric',
                   hoverongaps = False, showlegend = False,
                   zmin= 0,
                   zmax = 1.0),1,1)
                                     
                  
    fig.add_trace(go.Heatmap(
                    z=[[1.        , 0.94292854, 0.94815672, 0.87202437, 0.94562216,
        0.99231819, 0.9385546 , 0.9494511 , 0.91084651, 0.89149544],
       [0.94292854, 1.        , 0.93312181, 0.86525101, 0.99009811,
        0.94150048, 0.99861554, 0.93240262, 0.90845475, 0.89901379],
       [0.94815672, 0.93312181, 1.        , 0.86175513, 0.94634642,
        0.94882197, 0.93192513, 0.99331364, 0.88633525, 0.85914015],
       [0.87202437, 0.86525101, 0.86175513, 1.        , 0.88750488,
        0.8871494 , 0.8663091 , 0.86374241, 0.97228784, 0.89806194],
       [0.94562216, 0.99009811, 0.94634642, 0.88750488, 1.        ,
        0.95320559, 0.99108285, 0.94022444, 0.92058331, 0.90537072],
       [0.99231819, 0.94150048, 0.94882197, 0.8871494 , 0.95320559,
        1.        , 0.93928926, 0.94678264, 0.92414077, 0.90491567],
       [0.9385546 , 0.99861554, 0.93192513, 0.8663091 , 0.99108285,
        0.93928926, 1.        , 0.92986185, 0.90986309, 0.89773304],
       [0.9494511 , 0.93240262, 0.99331364, 0.86374241, 0.94022444,
        0.94678264, 0.92986185, 1.        , 0.88803996, 0.86341196],
       [0.91084651, 0.90845475, 0.88633525, 0.97228784, 0.92058331,
        0.92414077, 0.90986309, 0.88803996, 1.        , 0.93925371],
       [0.89149544, 0.89901379, 0.85914015, 0.89806194, 0.90537072,
        0.90491567, 0.89773304, 0.86341196, 0.93925371, 1.        ]],
                   x=['1U07', '1IHR (A)', '2ABL', '1OPK (A)', '1QVC (A)','1QVC (B)','1PBG','1HZ6(A)','1OPK','2JWW'],
                   y=['1U07', '1IHR (A)', '2ABL', '1OPK (A)', '1QVC (A)','1QVC (B)','1PBG','1HZ6(A)','1OPK','2JWW'],
                    colorscale = 'Electric',
                   hoverongaps = False, showlegend = False,
                   zmin= 0,
                   zmax = 1.0),1,2)
                                     
    fig.add_trace(go.Heatmap(
                  z = [[1.        , 0.85283207, 0.84939342, 0.74864188, 0.87894559,
        0.86864809, 0.85346091, 0.86455338, 0.79759875, 0.59490699],
       [0.85283207, 1.        , 0.88597178, 0.77192051, 0.98391655,
        0.84972126, 0.99107772, 0.89218308, 0.77104034, 0.65558052],
       [0.84939342, 0.88597178, 1.        , 0.73801217, 0.89489107,
        0.8723865 , 0.87983882, 0.98755309, 0.70916111, 0.54115045],
       [0.74864188, 0.77192051, 0.73801217, 1.        , 0.79370191,
        0.66475065, 0.78434576, 0.77026421, 0.89142627, 0.65187442],
       [0.87894559, 0.98391655, 0.89489107, 0.79370191, 1.        ,
        0.88003478, 0.98546754, 0.89736794, 0.7935529 , 0.67653398],
       [0.86864809, 0.84972126, 0.8723865 , 0.66475065, 0.88003478,
        1.        , 0.84187869, 0.84326493, 0.66790049, 0.66496785],
       [0.85346091, 0.99107772, 0.87983882, 0.78434576, 0.98546754,
        0.84187869, 1.        , 0.88812621, 0.78333947, 0.65718255],
       [0.86455338, 0.89218308, 0.98755309, 0.77026421, 0.89736794,
        0.84326493, 0.88812621, 1.        , 0.74641578, 0.52987401],
       [0.79759875, 0.77104034, 0.70916111, 0.89142627, 0.7935529 ,
        0.66790049, 0.78333947, 0.74641578, 1.        , 0.68614487],
       [0.59490699, 0.65558052, 0.54115045, 0.65187442, 0.67653398,
        0.66496785, 0.65718255, 0.52987401, 0.68614487, 1.        ]],
                   x=['1U07', '1IHR (A)', '2ABL', '1OPK (A)', '1QVC (A)','1QVC (B)','1PBG','1HZ6(A)','1OPK','2JWW'],
                   y=['1U07', '1IHR (A)', '2ABL', '1OPK (A)', '1QVC (A)','1QVC (B)','1PBG','1HZ6(A)','1OPK','2JWW'],
                   colorscale = 'Electric',
                   hoverongaps = False, showlegend = False,
                   zmin= 0,
                   zmax = 1.0),1,3)
                                        
                             
   
    
    my_poster.add_section(title="Methods",
                          text="PDB files are used to gather protein characteristics such as residue type, polar group,\
                                and secondary structures. From these PDB files, C⍺-C⍺ Distance Matrices are derived to create\
                                our protein graph structure. Protein graphs are constructed with each C⍺ atom in the protein \
                                representing the characteristics of each residues as nodes. The C⍺-C⍺ distances as well as other\
                                features represent the graph edges. \
                                Protein graphs are passed through the marginalized graph kernel.  A similarity \
                                matrix is generated and normalized to a scale ranging from 0 to 1 with a \
                                rating of 1 meaning an exact match of proteins.\
                                Below is a figure showing the process creating a protein graph for the protein \
                                with PDB code 1OPK.",
                           img={"filename":"Picture1.png", "height":"4.125in", "width":"11in", "caption":""})
    my_poster.add_section(title="Results",
                          text="Using a test set of 10 PDB proteins the effect of the node sub-kernels on protein graph\
                          similarity was explored. This test set included proteins of similar structure with dissimilar\
                          sequence with other proteins with similar structure with dissimilar sequence as well as the protein\
                          PDB  2JWW with neither similar sequence nor structure to the rest of the set. The graph kernel \
                          was able to identify node-wise similarities. Three separate kernels were built with the node \
                          sub-kernel compared the Residue type, Secondary Structure, and both these features in all\
                          nodes.  \
                          The node kernel was able to identify high similarity between protein chains and their parent\
                          protein. It failed to identify 2JWW as dissimilar to the test set when only comparing residue\
                          type in the node sub-kernel.",
                          plot={"fig":fig,"caption":"Effects of Node Features Compared in Sub-Kernel on Protein Similarity-\
                                 Parentheses denote Protein Chain"})
    
    my_poster.next_column()

    # Add sections to third column then add new column
    
   
 
    my_poster.add_section(title="Discussion",
                          text="While exploring the node sub-kernel it was found that the definition of protein pair-wise \
                                similarity was largely dependent on the construction of the node sub-kernel. This method is \
                                capable of matching segments of a protein to itself. An instance of this   ")
        #img = {"filename": "Protein_Graph_Process.png", "height": "6in", "width":"8in", "caption":""})                 
        
       
    my_poster.add_section(title="Future Work", 
                          text="The focus of this work was on understanding the abilities \
                                of the node kernel. Still there remains work to be done with the edge \
                                sub kernel. Plans are to include other representations of the edge such\
                                as hydrogen bonds and interaction forces. This would allow for a more physical\
                                understanding of the edges effect on the graph kernel. Another point of interest\
                                is creating a method that allows for subgraphs of the protein graphs to\
                                be formed in order to find points of high similarity between different proteins.")
    my_poster.add_section(title="Conclusion", 
                          text="Use of a marginalized graph kernel is a valid method to compute pairwise \
                                similarity between protein graphs. This method allows for the identification of\
                                structural, physical, and chemical similarities of protein graphs. Use of the node\
                                sub-kernel was essential in starting the development of differentiating between \
                                the protein characteristics. \
                                Comparing protein structures with a graph kernel is a valid way of finding \
                                pairwise similarities. In the future,  plans are to use this method to create \
                                a diverse set of proteins for a ML algorithm to predict Coarse Grain potential\
                                groups for a Molecular Dynamics method.")
    my_poster.add_section(title="Acknowledgements", 
                          text="This work was supported in part by the U.S. Department of \
                                Energy, Office of Science, Office of Workforce Development for Teachers \
                                and Scientists (WDTS) under the Berkeley Lab Undergraduate Faculty Fellowship \
                                (VFP) program. Thank you to Yu-Hang Tang for developing the graph kernel package\
                                used in this project as well as to Silvia Crivelli and Masakatsu Watanabe for their \
                                help and suggestions. Computing allocations were provided through NERSC.")
    my_poster.next_column()

    return my_poster.compile()

# **********************************************************************

# Dash App Configuration
if RUN_LOCAL:
    app = dash.Dash(__name__,
                    assets_folder= str(Path(__file__).parent.absolute())+"/assets",
                    assets_url_path='/',
                    external_stylesheets=[dbc.themes.BOOTSTRAP],
                    suppress_callback_exceptions=True)
else:
    server = flask.Flask(__name__)
    server.secret_key = os.environ.get('secret_key', str(randint(0, 1000000)))
    app = dash.Dash(__name__,
                    server=server,
                    assets_folder= str(Path(__file__).parent.absolute())+"/assets",
                    assets_url_path='/',
                    external_stylesheets=[dbc.themes.BOOTSTRAP],
                    suppress_callback_exceptions=True)
app.layout = create_poster()

# Main Function
if __name__ == "__main__":
    if RUN_LOCAL:
        app.run_server(debug=False, host="0.0.0.0", port="8888")
    else:
        app.server.run(debug=True, threaded=True)

        
        
        
    