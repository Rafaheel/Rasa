# Rasa<p align="center">
   <img src="./img/rasa.jpg" alt="Turma" width="400"/>   
</p>
<p align="center">ChatBot made with Rasa: PWith Rasa, all teams can create personalized, automated interactions with customers, at scale. Rasa provides infrastructure & tools necessary for building the very best assistants - ones that meaningfully transform how customers communicate with businesses. <br>
</p>

# :Computer: Technologies and 🛠️ Tools to run this project
<ul>
 <li><a href="https://rasa.com/docs/rasa/installation/">Rasa</a></li>
 <li><a href="https://code.visualstudio.com/">Visual Studio Code</a></li>
 <li><a href="https://rasa.com/docs/rasa-x/installation-and-setup/installation-guide">Rasa x</a></li>
 <li><a href="https://www.anaconda.com/">Anaconda</a></li>
 <li><a href="https://github.com/">Github</a></li>
 <li><a href="https://support.microsoft.com/en-us/topic/the-latest-supported-visual-c-downloads-2647da03-1eea-4433-9aff-95f26a218cc0">C++ visual install</a></li>
</ul>

# Screenshots
<div style="display: flex; flex-direction: 'row'; align-items: 'center';">
   <img src="public/images/web-landing.png" width="400px">
   <img src="public/images/web-list.png" width="400px">
</div>

<h4>   &#127919&#128187| Stacks that we using: </h4>
<p align="left">
<img src="./img/rasa.jpg" alt="rasa"  width="35" height="35"/>
<img src="./img/anaconda.png" alt="anaconda"  width="35" height="35"/>
<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="35" height="35"/>
</p><p align="center">

### 📦 How to install

```bash
- Before you installed Anaconda packge and C++visual install, on your terminal you must run:

    - conda create --name NAME python==3.8 (to create your envarioment)
    - conda activate NAME (activate your envarioment)
    - conda install ujson (y when prompted)
    - conda install tensorflow (y when prompted)
    - pip install rasa==2.8.2
    - pip install rasa-sdk==2.8.1
    - pip install rasa-x==0.39.3 --extra-index-url https://pypi.rasa.com/simple 
    - pip3 install SQLAlchemy==1.3.22
    - pip install sanic-jwt==1.6.0


When all set run:
    - rasa init (to create your first project)
    - This comand create your first model and ask you want train your model for the first time (if you set no in this part, you could run whit rasa train command later)
    - If you want train your model with rasa x envarioment follow this steps:
        - Activate your envarioment
        - You need change this specific part in your endpoins.yml file:
            - change the value of "action_endpoint" to http://127.0.0.1:5055/webhook in url part
        - Run you actions state with run rasa actions command
        - Open another terminal and run rasa x command


```

- Feel free to follow this tutorials:
  <li><a href="https://www.youtube.com/watch?v=GlR60CvTh8A">Rasa YouTube</a></li>
  <li><a href="https://www.youtube.com/watch?v=YweVKcio1-Y">Rasa YouTube</a></li>




