color[] colors = 
{ 
  color(192),
  color(255, 255, 0), 
  color(255, 165, 0),
  color(255, 0, 0),
  color(0, 255, 0),
  color(0, 0, 255),
  color(148,0,211)
};
int c_color = 0;
float blockSize = 50;
float spacing = 5;

void setup()
{
  size(600, 600);
  rectMode(CENTER);
}

void draw() 
{
  background(0);
  textSize(32);
  text("click to change color!", 180, 180);
  
  for (int i = 0; i < 3; i++) {
    for (int j = 0; j < 3; j++) {
      float rectX = 250 + i * (blockSize + spacing); 
      float rectY = 250 + j * (blockSize + spacing); 
      float distance = dist(rectX, rectY, mouseX, mouseY);
      
      if (distance < blockSize / 2) {
        
        float randomX = random(-10, 10); 
        float randomY = random(-10, 10);
        rectX += randomX;
        rectY += randomY;
        fill(255,255,50);
        text(":happy happy happy!", rectX, rectY-50);
    }
      fill(colors[c_color]);
      rect(rectX, rectY, blockSize, blockSize);
    }
  }
}

void mousePressed()
{
  c_color = (c_color + 1) % colors.length;
}
