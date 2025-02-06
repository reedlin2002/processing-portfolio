ArrayList<Particle> particles;
int countdown = 5;
int numFireflies = 25;
float[] posX = new float[numFireflies];
float[] posY = new float[numFireflies];
float[] speedX = new float[numFireflies];
float[] speedY = new float[numFireflies];
float[] fireflySize = new float[numFireflies];
color[] fireflyColors = new color[numFireflies];
float NYfontSize = 64;
float NYdelta = 0.3;
color[] colors = { #FF0000, #FF7F00, #FFFF00, #00FF00, #0000FF, #00F100 }; // 彩虹顏色

void setup() {
  size(800, 600);
  background(0); 
  textSize(64);
  initializeFireflies();
  textAlign(CENTER, CENTER);
}

void draw() {
  background(76,0,153);
  timer();
  moveFireflies();
  building();
  Moon();
  Grass();
  if (particles != null) {
    for (Particle p : particles) {
      p.move();
      p.display();
    }
  }
}

void timer(){
  if (countdown > 0) {
    textSize(64);
    fill(255);
    text(countdown, width/2, height/4);
  } 
  else if (countdown <= 0) {
    NewYearText();
  }
  
  if (frameCount % 60 == 0 && countdown > 0) {
    countdown--;
  }
}

void Grass() { //草地
  fill(34, 139, 34); //綠色
  rect(0, 500, 800, 200); 
}

void Moon() { //月亮
  float moonX = 650; // 月亮的位置
  float moonY = 140;
  float distance = dist(mouseX, mouseY, moonX, moonY); // 計算滑鼠位置與月亮的距離
  
  noStroke();
  fill(255, 255, 204); 
  if (distance < 60) { // 當滑鼠靠近月亮時
    moonX += random(-2, 2); // 隨機改變月亮的位置
    moonY += random(-2, 2);
    textSize(24);
    if(countdown >0)
    {
      text("? ? ?", moonX-100, moonY-70);
    }
    else text("Happy New Year!", moonX-100, moonY-70);
  }
  ellipse(moonX, moonY, 120, 120);
}

void building() {
  noStroke();
  fill(100);
  rect(100, 150, 100, 400); // 建築物主體
  fill(255, 255, 204);
  // 第一扇窗戶
  rect(150, 250, 20, 30);
  // 第二扇窗戶
  rect(150, 200, 20, 30);
  
  fill(0,0,51);
  rect(200, 250, 100, 400); // 建築物主體
  fill(255, 255, 204);
  // 第一扇窗戶
  rect(230, 330, 20, 30);
  // 第二扇窗戶
  rect(270, 320, 20, 30);
  
  fill(96,96,96);
  rect(0, 200, 100, 400); // 建築物主體
  fill(255, 255, 204);
  // 第一扇窗戶
  rect(10, 250, 20, 30);
  // 第二扇窗戶
  rect(50, 350, 20, 30);
  rect(50, 400, 20, 30);
}

void NewYearText(){
  textSize(NYfontSize);
  int index = int(frameCount / 30) % colors.length; // 控制顏色變換速度
  fill(colors[index]);
  text("Happy New Year!", width / 2, height / 4);

  NYfontSize = map(sin(frameCount * NYdelta), -1, 1, 24, 40); // 放大縮小效果
}
// 初始化螢火蟲
void initializeFireflies() {
  for (int i = 0; i < numFireflies; i++) {
    posX[i] = random(width); // 隨機設定螢火蟲的 X 座標
    posY[i] = random(height); // 隨機設定螢火蟲的 Y 座標
    speedX[i] = random(-1, 1); // 隨機設定螢火蟲的 X 方向速度
    speedY[i] = random(-1, 1); // 隨機設定螢火蟲的 Y 方向速度
    fireflySize[i] = random(2, 5); // 隨機設定螢火蟲的大小
    fireflyColors[i] = color(200, 255, 0); // 螢火蟲的顏色設定為黃色
  }
}

// 移動螢火蟲
void moveFireflies() {
  for (int i = 0; i < numFireflies; i++) {
    posX[i] += speedX[i]; // 更新螢火蟲的 X 座標
    posY[i] += speedY[i]; // 更新螢火蟲的 Y 座標

    if (posX[i] > width || posX[i] < 0) { // 檢查是否超出畫布邊界
      posX[i] = random(width); // 若超出邊界，重新定位到畫布內的隨機位置
    }
    if (posY[i] > height || posY[i] < 0) {
      posY[i] = random(height);
    }

    drawFirefly(posX[i], posY[i], fireflySize[i], fireflyColors[i]); // 繪製螢火蟲
  }
}

// 繪製單個螢火蟲的函數
void drawFirefly(float x, float y, float size, color col) {
  fill(col);
  noStroke();
  ellipse(x, y, size, size);
}


void mousePressed() {
  createFirework(mouseX, mouseY);
}

void createFirework(int x, int y) {
  particles = new ArrayList<Particle>();
  for (int i = 0; i < 100; i++) {
    particles.add(new Particle(x, y));
  }
}

// 煙火
class Particle {
  float x, y;
  float speedX, speedY;
  color col;

  Particle(float x, float y) {
    this.x = x;
    this.y = y;
    this.speedX = random(-5, 5);
    this.speedY = random(-5, 5);
    this.col = color(random(255), random(255), random(255));
  }

  //更新位置
  void move() {
    x += speedX;
    y += speedY;
  }
  // 顯示粒子
  void display() {
    noStroke();
    fill(col);
    ellipse(x, y, 5, 5); //圓形
  }
}
