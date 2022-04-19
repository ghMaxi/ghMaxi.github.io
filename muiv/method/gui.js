class DrawObject
{
    constructor() { draw_objects.push(this); }
    static all() { return draw_objects; }
}
function run_gui()
{
    canvas_element = document.getElementsByTagName("canvas")[0];
    tool = canvas_element.getContext("2d");
    function draw_gui()
    {
        tool.fillStyle = 'white';
        tool.fillRect(0, 0, canvas_element.width, canvas_element.height);
        for (id in draw_objects)
        {
            draw_objects[id].draw(tool);
        }
    }
    setInterval(draw_gui, 17);
}
run_gui();

class Rectangle extends DrawObject {
  constructor(x, y, height, width, color) {
    super();
    this.x = x;
    this.y = y;
    this.height = height;
    this.width = width;
    this.color = color;
  }
  move(x, y)
  {
      this.x += x;
      this.y += y;
  }
  draw(tool)
  {
    tool.fillStyle = this.color;
    tool.fillRect(this.x, this.y, this.width, this.height);
    tool.fillStyle = 'teal';
    tool.fillText("test", this.x + 3, this.y + 9);
    tool.strokeStyle = 'rgb(0, 0, 100)';
    tool.strokeRect(this.x, this.y, this.width, this.height);
  }
}
new Rectangle(10, 10, 20, 20, 'blue');
new Rectangle(30, 30, 50, 100, 'red');
