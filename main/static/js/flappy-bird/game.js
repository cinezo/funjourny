var bird;
var pipes = [];
var score = 0;

function save_score(new_score) {
  $('#newscore').val(new_score);
  $('#submit').click();
}

function setup() {
  createCanvas(640, 480);
  bird = new Bird();
  pipes.push(new Pipe());
}

function draw() {
  background(0);
  textSize(30);
  text(score.toString(), width/2, height / 10);
  textAlign(CENTER, TOP);
  for (var i = pipes.length - 1; i >= 0; i--) {
    pipes[i].show();
    pipes[i].update();

    if (pipes[i].hits(bird)) {
      pipes = [];
      if (score >= current_score) {
        current_score = score;
        save_score(score);
      } else {
        score = 0;
        return;
      }
      score = 0;
      return;
    }

    if (pipes[i].offscreen()) {
      pipes.splice(i, 1);
    }
  }

  bird.update();
  bird.show();

  if (frameCount % 75 == 0) {
    pipes.push(new Pipe());
  }
  
  if (frameCount % 5 == 0) {
    score++;
  }
}

function keyPressed() {
  if (key == ' ') {
    bird.up();
    //console.log("SPACE");
  }
}