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
