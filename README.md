# Hextech-Automatic-Page-Turner
Powered by the Hextech muscle board, the automatic page turner is used to flip sheet music on a music stand avoiding the need of a page flipper and preventing a muscian from stopping during a song. 

# MQTT Server
The HexTech muscle board receives input through an MQTT Server. An MQTT client, the HexTech board, establishes a connection with the MQTT broker. When the MQTT broker receives a message, it forwards it to subscribers (the HexTech board).

The software, programmed in Python, can publish messages to the MQTT broker.

# Demo Video
A video of the robot operating can be found and downloaded in [Demo (3).mp4](DEMO%20(3).mp4)

# Assembly 
Pictures, materials, and explanations of  assembly are provided in the file. 
[Automatic Page Turner PDF](./Automatic%20Page%20Turner.pdf) 

# Code Overview
The code was completed in VSCode using python from the Hextech Library. The completed code used is found in [Auto Page Turner](Hextech-Automatic-Page-Turner/CODE/auto%20page%20turner) . 
EX: Moving stepper motors --> [muscle.stepper1.move().run()]



# Challenges (possible)
- Multiple or no pages flipped
- Adhesive needs to be replaced

# Lessons Learned
Before I built this robot and heard about Hextech I was not too familiar with coding, how motors worked, or how to build a robot from ground zero, but now I understand the many intricicies of how stepper motors function, how to successfully create a mchine, and how to effectively control hardware. Due to Hextech, I continue to grow my knowledge and experience in engineering quickly being able to interact mechanical components I build with python code I write. 
