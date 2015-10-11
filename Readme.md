# Multicraft

A simple Python script to create and run new Minecraft Server instances on the same server. It leverages Docker and finds a free port on the system to run it.

## Installation

Just download multicraft.py to your favourite folder :)

## Requirements

1. A Minecraft Docker container, e.g.: https://github.com/overshard/docker-minecraft (You'll have to hack multicraft.py a bit to adapt it to your container's name, which is "mcdocker" by default)
2. [Docker-py](https://github.com/docker/docker-py)
3. A Linux system to run all this

## Usage

Just run it locally on a Linux system running Docker.

Example:

    user@Server:~/repos/multicraft$ sudo ./multicraft.py
    Instance ID: 9566729284dfc39cebd5f76a9987d8d86202190433cd4216fbc5c3ed140457dc
    Listening on port 25565
    user@Server:~/repos/multicraft$ sudo docker ps
    CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS                      NAMES
    9566729284df        mcdocker            "/start"            5 seconds ago       Up 4 seconds        0.0.0.0:25565->25565/tcp   sharp_bohr
    user@Server:~/repos/multicraft$ sudo ./multicraft.py
    Instance ID: a7212a66027096d462e8479bad20051f277ed65761ce4dfb95c0bd26adee5cec
    Listening on port 25566
    user@Server:~/repos/multicraft$ sudo docker ps
    CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS                      NAMES
    a7212a660270        mcdocker            "/start"            3 seconds ago       Up 2 seconds        0.0.0.0:25566->25565/tcp   goofy_turing
    9566729284df        mcdocker            "/start"            18 seconds ago      Up 17 seconds       0.0.0.0:25565->25565/tcp   sharp_bohr

As you can see above, the second instance maps port 25566 on the host to 25565 on the Minecraft service inside the container. The **/start** script downloads the jar file for Minecraft server 1.8.8 and starts the server. The Docker image is Isaac Bythewood's [docker-minecraft](https://github.com/overshard/docker-minecraft) with minimal changes (namely Minecraft Server's version).

I've limited this to 3 simultaneous instances by default, but this limit is easily changeable inside the script.

## Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D

## License

What?
