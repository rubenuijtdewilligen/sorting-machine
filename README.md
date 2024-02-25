# Sorting Machine
A machine for sorting anything using Raspberry Pi, Mindstorms and a PC. Originally created for chilli peppers. This repo contains code for lego bricks.

Read the paper [here](https://rbnu.nl/cdn/Machine_learning_computer_vision_applied_to_the_classification_of_vegetables_based_on_quality.docx).

## Raspberry Pi Installation Instructions

1. Update the Raspberry Pi's software
```SH
sudo apt-get update && sudo apt-get upgrade
```

2. Install git
```SH
sudo apt-get install git -y
```

3. Download the Node version manager install script and pipe it to bash to execute
```SH
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash
```

4. Add nvm to path
```SH
export NVM_DIR="$([ -z "${XDG_CONFIG_HOME-}" ] && printf %s "${HOME}/.nvm" || printf %s "${XDG_CONFIG_HOME}/nvm")"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
```

5. Use nvm to install the Node long term support versions
```SH
nvm install --lts
```

6. Clone this repository
```SH
git clone https://github.com/rubenuijtdewilligen/sorting-machine.git
```

7. Move the rpi folder to sorter/
```SH
mv sorting-machine/rpi/ sorter/
```

8. Remove the rest of the repository
```SH
rm -rf sorting-machine
```

9. Change directory to sorter/
```SH
cd sorter/
```

10. Use npm to install the required Node modules (only Express)
```SH
npm install
```

11. Execute the program
```SH
node .
```