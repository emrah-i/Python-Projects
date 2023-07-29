
var choice = Math.floor(Math.random() * 4)
item = $('#grid > *')[choice].id

simon = []
simon.push(item)

var level = $('#level').text()
level = parseInt(level)

clicks = []

$('#button button').click(function(){
    if (level == 1) {
        simon_play()
        check()
    }
    else {
        choose_new()
        check()
    }
})

$('#grid > *').click(function(){
    clicks.push(this.id)
    sound($(this).attr('id'), this)
})

function check(){
    setTimeout(()=>{
        if (areArraysEqual(clicks, simon)) {
            level++;
            $('#level').text(level)
            clicks = []
        }
        else {
            level = 1;
            $('#level').text(level)
            clicks = []
        }
    }, 3000)
}

function areArraysEqual(arr1, arr2) {
    if (arr1.length !== arr2.length) {
      return false;
    }
  
    for (let i = 0; i < arr1.length; i++) {
      if (arr1[i] !== arr2[i]) {
        return false;
      }
    }
  
    return true;
  }

function simon_play() {
    for (i=0; i<simon.length; i++) {
        if (i == 0) {
            sound(simon[i])
        }
        else {
            setTimeout(()=>{
                sound(simon[i])}, 2000)
        }
    } 
}

function choose_new(){
    var choice = Math.floor(Math.random() * 4)
    item = $('#grid > *')[choice].id
    simon.push(item)
    clicks = []
    simon_play()
}

function sound(color){

    item = $('#' + color)

    switch (color) {
        case 'g':
            var sound = new Audio('sounds/drum_1.mp3')
            sound.play()
            break;
        case 'r':
            var sound = new Audio('sounds/drum_2.mp3')
            sound.play()
            break;
        case 'y':
            var sound = new Audio('sounds/drum_4.mp3')
            sound.play()
            break;
        case 'b':
            var sound = new Audio('sounds/drum_5.mp3')
            sound.play()
            break; 
    }

    $(item).animate({opacity: .5})
    $(item).animate({opacity: 1})
}