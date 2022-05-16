function getRandomInt(max) {
  /* функция возвращает случайное целое от 0 до max */
  return Math.floor(Math.random() * max);
}

function draw(draw_tools) {
  var max_x = draw_tools.canvas.width;
  var max_y = draw_tools.canvas.height;
  for (var x = 0; x < 10000; x += 0.01) {
    var x2 = x - max_x / 2;
    var y = -x2 * x2 * 0.005 + max_y;
    draw_tools.fillRect(x, y, 1, 1);
  }
}

function runProgram() {
  /* функция получает canvas из HTML, достаёт из него инструментарий draw_tools
     и передаёт его процедуре рисования */
  canvas_element = document.getElementsByTagName("canvas")[0];
  draw_tools = canvas_element.getContext("2d");
  draw(draw_tools)
}

runProgram();








/*
alert("woota");
function draw_gui(tool)
{
    tool.fillStyle = 'blue';
    tool.fillRect(10, 10, 100, 100);
    tool.fillStyle = 'teal';
    tool.fillText("test", 1, 1);
    tool.strokeStyle = 'rgb(0, 0, 100)';
    tool.strokeRect(10, 10, 100, 100);
}
canvas_element = document.getElementsByTagName("canvas")[0];
draw_tools = canvas_element.getContext("2d");
draw_gui(draw_tools);
*/
