let list = document.querySelector('.equipas-slideshow .slideshow');
let items = document.querySelectorAll('.equipas-slideshow .slideshow .slide');
let prev = document.getElementById('anterior');
let next = document.getElementById('proximo');

let active = 0;
let lenghtItems = items.length - 1;

next.onclick = function (){
    if (active + 1 > lenghtItems){
        active = 0;
    }
    else{
        active += 1;
    }
    reloadSlider();
}

prev.onclick = function (){
    if (active - 1 < 0){
        active = lenghtItems;
    }
    else{
        active -= 1;
    }
    reloadSlider();
}

let refreshSlider = setInterval(()=> {next.click()}, 3000)

function reloadSlider(){
    let checkLeft = items[active].offsetLeft;
    list.style.left = -checkLeft + "px";
    clearInterval(refreshSlider)
    refreshSlider = setInterval(()=> {next.click()}, 3000)
}

//--------------------------------------------------------------------------------------------

  var currentButtons = {};

  function toggleButton(buttonId, containerId) {
    var containerButtons = currentButtons[containerId] || [];
    var button = document.getElementById(buttonId);

    if (containerButtons.includes(button)) {
      button.classList.remove("checked");
      containerButtons = containerButtons.filter(btn => btn !== button);
    } else {
      containerButtons.forEach(function(btn) {
        btn.classList.remove("checked");
      });
      button.classList.add("checked");
      containerButtons = [button];
    }

    currentButtons[containerId] = containerButtons;
  }

//--------------------------------------------------------------------------------------------

document.addEventListener("DOMContentLoaded", function() {
    console.log("DOMContentLoaded event fired");
    var characterDivs = document.querySelectorAll('.planet-waves-container img');
    characterDivs.forEach(function(div) {
        console.log("Adding hide1 class to img element");
        div.classList.add('hide1');
    });
});

document.addEventListener("DOMContentLoaded", function() {
    console.log("DOMContentLoaded event fired");
    var characterDivs = document.querySelectorAll('.klee > div[class$="-bot"]');
    characterDivs.forEach(function(div) {
        console.log("Adding hide1 class to Klee's div");
        div.classList.add('hide1');
    });
});

document.addEventListener("DOMContentLoaded", function() {
    console.log("DOMContentLoaded event fired");
    var characterDivs = document.querySelectorAll('.ayaka > div[class$="-bot"]');
    characterDivs.forEach(function(div) {
        console.log("Adding hide1 class to Ayaka's div");
        div.classList.add('hide1');
    });
});

document.addEventListener("DOMContentLoaded", function() {
    console.log("DOMContentLoaded event fired");
    var characterDivs = document.querySelectorAll('.ningguang > div[class$="-bot"]');
    characterDivs.forEach(function(div) {
        console.log("Adding hide1 class to Ningguang's div");
        div.classList.add('hide1');
    });
});

document.addEventListener("DOMContentLoaded", function() {
    console.log("DOMContentLoaded event fired");
    var characterDivs = document.querySelectorAll('.zhongli > div[class$="-bot"]');
    characterDivs.forEach(function(div) {
        console.log("Adding hide1 class to Zhongli's div");
        div.classList.add('hide1');
    });
});

document.addEventListener("DOMContentLoaded", function() {
    console.log("DOMContentLoaded event fired");
    var characterDivs = document.querySelectorAll('.klee > div[class$="-textos"]');
    characterDivs.forEach(function(div) {
        console.log("Adding hide1 class to Klee's text div");
        div.classList.add('hide1');
    });
});

document.addEventListener("DOMContentLoaded", function() {
    console.log("DOMContentLoaded event fired");
    var characterDivs = document.querySelectorAll('.ayaka > div[class$="-textos"]');
    characterDivs.forEach(function(div) {
        console.log("Adding hide1 class to Ayaka's text div");
        div.classList.add('hide1');
    });
});

document.addEventListener("DOMContentLoaded", function() {
    console.log("DOMContentLoaded event fired");
    var characterDivs = document.querySelectorAll('.ningguang > div[class$="-textos"]');
    characterDivs.forEach(function(div) {
        console.log("Adding hide1 class to Ningguang's text div");
        div.classList.add('hide1');
    });
});

document.addEventListener("DOMContentLoaded", function() {
    console.log("DOMContentLoaded event fired");
    var characterDivs = document.querySelectorAll('.zhongli > div[class$="-textos"]');
    characterDivs.forEach(function(div) {
        console.log("Adding hide1 class to Zhongli's text div");
        div.classList.add('hide1');
    });
});

function moveDiv1(character) {
    console.log("moveDiv1 function called with character: " + character);
    var container = document.querySelector('.planet-waves-container');
    var characterDivImg = container.querySelector('.' + character + ' img');
    var characterDivItems = container.querySelector('.' + character + ' .' + character + '-bot');
    var characterDivItemsDescr = container.querySelector('.' + character + ' .' + character + '-textos');
    var allDivs = container.querySelectorAll('div[class$="-rad"]');
    var allCharacterDivsImg = container.querySelectorAll('.planet-waves-container > div img');
    var allCharacters = container.querySelectorAll('.planet-waves-container > div');
    var allCharacterDivsItems = [];

    allCharacters.forEach(function(character) {
        allCharacterDivsItems.push(container.querySelectorAll('.'+character.classList[0]+' > div'));
    });

    console.log("All characters: ", allCharacters);
    console.log("All character div items: ", allCharacterDivsItems);
    console.log("Character Image: ", characterDivImg);
    console.log("Character Items: ", characterDivItems);

    allCharacterDivsImg.forEach(function(div) {
        console.log("Adding hide2 class to all img elements");
        div.classList.add('hide2');
    });

    for (let i = 0; i < allCharacterDivsItems.length; i++) {
        allCharacterDivsItems[i].forEach(function(div) {
            console.log("Adding hide2 class to div items");
            div.classList.add('hide2');
        });
    }

    characterDivImg.classList.remove('hide2');
    characterDivImg.classList.remove('hide1');
    characterDivItems.classList.remove('hide2');
    characterDivItems.classList.remove('hide1');
    characterDivItemsDescr.classList.remove('hide2');
    characterDivItemsDescr.classList.remove('hide1');

    container.classList.remove('show1');

    setTimeout(function() {
        console.log("Adding show1 class to images and items");
            characterDivImg.classList.add('show1');
            characterDivItems.classList.add('show1');
            characterDivItemsDescr.classList.add('show1');
    }, 0);

    return allCharacters;
}

//--------------------------------------------------------------------------------------------

function scrollToSection(where) {
        var section = document.getElementById(where);
        if (section) {
            var top_movement = section.offsetTop + 250;
            window.scrollTo({
                top: top_movement,
                behavior: 'smooth'
            });
        } else {
            alert("Section not found!");
        }
    }

//--------------------------------------------------------------------------------------------

document.addEventListener("DOMContentLoaded", function() {
    console.log("DOMContentLoaded event fired");
    var characterDivs = document.querySelectorAll('.planet-waves-container img');
    characterDivs.forEach(function(div) {
        console.log("Adding hide3 class to img element");
        div.classList.add('hide3');
    });
});

document.addEventListener("DOMContentLoaded", function() {
    console.log("DOMContentLoaded event fired");
    var characterDivs = document.querySelectorAll('.raiden > div[class$="-bot"]');
    characterDivs.forEach(function(div) {
        console.log("Adding hide3 class to Raiden's div");
        div.classList.add('hide3');
    });
});

document.addEventListener("DOMContentLoaded", function() {
    console.log("DOMContentLoaded event fired");
    var characterDivs = document.querySelectorAll('.xingqiu > div[class$="-bot"]');
    characterDivs.forEach(function(div) {
        console.log("Adding hide3 class to Xingqiu's div");
        div.classList.add('hide3');
    });
});

document.addEventListener("DOMContentLoaded", function() {
    console.log("DOMContentLoaded event fired");
    var characterDivs = document.querySelectorAll('.xiangling > div[class$="-bot"]');
    characterDivs.forEach(function(div) {
        console.log("Adding hide3 class to Xiangling's div");
        div.classList.add('hide3');
    });
});

document.addEventListener("DOMContentLoaded", function() {
    console.log("DOMContentLoaded event fired");
    var characterDivs = document.querySelectorAll('.bennett > div[class$="-bot"]');
    characterDivs.forEach(function(div) {
        console.log("Adding hide1 class to Bennett's div");
        div.classList.add('hide3');
    });
});

document.addEventListener("DOMContentLoaded", function() {
    console.log("DOMContentLoaded event fired");
    var characterDivs = document.querySelectorAll('.raiden > div[class$="-textos"]');
    characterDivs.forEach(function(div) {
        console.log("Adding hide1 class to Raiden's text div");
        div.classList.add('hide3');
    });
});

document.addEventListener("DOMContentLoaded", function() {
    console.log("DOMContentLoaded event fired");
    var characterDivs = document.querySelectorAll('.xingqiu > div[class$="-textos"]');
    characterDivs.forEach(function(div) {
        console.log("Adding hide1 class to Xingqiu's text div");
        div.classList.add('hide3');
    });
});

document.addEventListener("DOMContentLoaded", function() {
    console.log("DOMContentLoaded event fired");
    var characterDivs = document.querySelectorAll('.xiangling > div[class$="-textos"]');
    characterDivs.forEach(function(div) {
        console.log("Adding hide1 class to Xiangling's text div");
        div.classList.add('hide3');
    });
});

document.addEventListener("DOMContentLoaded", function() {
    console.log("DOMContentLoaded event fired");
    var characterDivs = document.querySelectorAll('.bennett > div[class$="-textos"]');
    characterDivs.forEach(function(div) {
        console.log("Adding hide1 class to Bennett's text div");
        div.classList.add('hide3');
    });
});

function moveDiv2(character) {
    console.log("moveDiv2 function called with character: " + character);
    var container = document.querySelector('.d4c-container');
    var characterDivImg = container.querySelector('.' + character + ' img');
    var characterDivItems = container.querySelector('.' + character + ' .' + character + '-bot');
    var characterDivItemsDescr = container.querySelector('.' + character + ' .' + character + '-textos');
    var allDivs = container.querySelectorAll('div[class$="-rad"]');
    var allCharacterDivsImg = container.querySelectorAll('.d4c-container > div img');
    var allCharacters = container.querySelectorAll('.d4c-container > div');
    var allCharacterDivsItems = [];

    allCharacters.forEach(function(character) {
        allCharacterDivsItems.push(container.querySelectorAll('.'+character.classList[0]+' > div'));
    });

    console.log("All characters: ", allCharacters);
    console.log("All character div items: ", allCharacterDivsItems);
    console.log("Character Image: ", characterDivImg);
    console.log("Character Items: ", characterDivItems);


    allCharacterDivsImg.forEach(function(div) {
        console.log("Adding hide4 class to all img elements");
        div.classList.add('hide4');
    });

    for (let i = 0; i < allCharacterDivsItems.length; i++) {
        allCharacterDivsItems[i].forEach(function(div) {
            console.log("Adding hide4 class to div items");
            div.classList.add('hide4');
        });
    }

    characterDivImg.classList.remove('hide4');
    characterDivImg.classList.remove('hide3');
    characterDivItems.classList.remove('hide4');
    characterDivItems.classList.remove('hide3');
    characterDivItemsDescr.classList.remove('hide4');
    characterDivItemsDescr.classList.remove('hide3');

    container.classList.remove('show2');

    setTimeout(function() {
        console.log("Adding show2 class to images and items");
            characterDivImg.classList.add('show2');
            characterDivItems.classList.add('show2');
            characterDivItemsDescr.classList.add('show2');
    }, 0);

    return allCharacters
}

//--------------------------------------------------------------------------------------------

function revealDiv1(item, character) {
    var container = document.querySelector('.planet-waves-container');
    var characterDivItemsDescr = container.querySelector('.' + character + '-textos');
    var itemDescr = characterDivItemsDescr.querySelector('.texto-' + item);
    var allItems = [];
    var allCharacters = container.querySelectorAll('.planet-waves-container > div');
    var allCharacterDivsItems = [];

    console.log("All Characters: ", allCharacters)

    allCharacters.forEach(function(character) {
        allCharacterDivsItems.push(container.querySelectorAll('.'+character.classList[0]+' > div'));
    });

    console.log("All Character Divs Items: ", allCharacterDivsItems)

    allCharacterDivsItems.forEach(function(doubleDiv) {
        allItems.push(container.querySelectorAll('.'+doubleDiv[1].classList[0]+' > div'));
    });

    console.log('All Items: ', allItems);

    var allCharacterDivItemsDescr = [];

    allItems.forEach(function(item){
        allCharacterDivItemsDescr.push(item[0]);
        allCharacterDivItemsDescr.push(item[1]);
    });

    console.log('All Character Items Descriptions: ', allCharacterDivItemsDescr);


    allCharacterDivItemsDescr.forEach(function(div) {
        div.classList.add('vanish');
        div.classList.remove('reveal')
    });

    itemDescr.classList.remove('vanish');
    container.classList.remove('vanish');



    setTimeout(function() {
        itemDescr.classList.add('reveal');
    }, 500);
}

function revealDiv2(item, character) {
    var container = document.querySelector('.d4c-container');
    var characterDivItemsDescr = container.querySelector('.' + character + '-textos');
    var itemDescr = characterDivItemsDescr.querySelector('.texto-' + item);
    var allItems = [];
    var allCharacters = container.querySelectorAll('.d4c-container > div');
    var allCharacterDivsItems = [];

    console.log("All Characters: ", allCharacters)

    allCharacters.forEach(function(character) {
        allCharacterDivsItems.push(container.querySelectorAll('.'+character.classList[0]+' > div'));
    });

    console.log("All Character Divs Items: ", allCharacterDivsItems)

    allCharacterDivsItems.forEach(function(doubleDiv) {
        allItems.push(container.querySelectorAll('.'+doubleDiv[1].classList[0]+' > div'));
    });

    console.log('All Items: ', allItems);

    var allCharacterDivItemsDescr = [];

    allItems.forEach(function(item){
        allCharacterDivItemsDescr.push(item[0]);
        allCharacterDivItemsDescr.push(item[1]);
    });

    console.log('All Character Items Descriptions: ', allCharacterDivItemsDescr);


    allCharacterDivItemsDescr.forEach(function(div) {
        div.classList.add('vanish');
        div.classList.remove('reveal')
    });

    itemDescr.classList.remove('vanish');
    container.classList.remove('vanish');



    setTimeout(function() {
        itemDescr.classList.add('reveal');
    }, 500);
}

//--------------------------------------------------------------------------------------------

var audio = document.getElementById("musiquinha");

        function toggleAudio() {
            if (audio.paused) {
                audio.play();
                document.getElementById("botaoPlay").innerHTML = "⏸";
            } else {
                audio.pause();
                document.getElementById("botaoPlay").innerHTML = "⏵";
            }
        }