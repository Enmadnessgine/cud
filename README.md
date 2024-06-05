<h2>About CUD</h2>
<strong>CUD</strong> - a project for <strong>transmitting the coordinates</strong> of a game character from the SAMP game and <strong>displaying the player’s position</strong> using a virtual map on the site. 
At the moment, the <strong>development of the project is suspended</strong> at the moment front-end implementation stage (the coordinate transfer functionality has already been implemented). 
On the client side (SAMP), there must be a <strong>Lua</strong> script that will collect coordinates and send them to the server (to the back-end of the site). 
The site is implemented in <strong>Python</strong> using the <strong>Django framework</strong>, and also uses the <strong>websocket</strong> protocol to transfer coordinates.

<hr>

<h2>Technologies:</h2>
<ul>
  <li>Python;</li>
  <li>Django 5.0.1 & Django Channels 4.0.0;</li>
  <li>Lua;</li>
  <li>Websocket;</li>
  <li>HTML + CSS;</li>
  <li>SQLite;</li>
  <li>JavaScript;</li>
</ul>

<hr>
<h2>How to install the project?</h2>
<h3>Install to client side:</h3>
<ol>
  <li>Install SAMP client;</li>
  <li>Install Moonloader library - https://www.blast.hk/threads/13305/</li>
  <li>Add file <strong>cud(getter cords).lua</strong> in folder Moonloader;</li>
  <li>Print to game chat command: <code>/scoords</code></li>
</ol>

<h3>Install to server side (site):</h3>
  <li>(Optional) Install python virtual enviroment:
  <code>python -m venv venv</code></li>
  <li>Install requirement libraries and framework:
    <ol>
      <li><code>pip install django</code></li>
      <li><code>python -m pip install -U channels</code></li>
      <li><code>pip install daphne channels</code></li>
      <li><code>daphne -b 0.0.0.0 -p 8001 myproject.asgi:application</code></li>
    </ol>
  </li>
</ol>

<hr>

<h2>Demonstration:</h2>

![error](https://github.com/Enmadnessgine/cud/blob/main/map1.jpg?raw=true)

