function ImageResource(url, width, height) {
    this.image = new Image();
    this.image.src = url;
    this.width = width;
    this.height = height;
}
ImageResource.prototype.draw = function(draw_tools, x, y) {
    if (this.image.complete && this.image.naturalHeight > 0) {
        draw_tools.drawImage(this.image, x, y, this.width, this.height);
    } else {
        draw_button(draw_tools, x, y, ":(", this.width/2 - 15, this.width, this.height / 2 + 10, this.height)
    }
}
main_menu_bg = new ImageResource("./images/main_menu_bg.jpg", 100, 100);

function draw(draw_tools) {
    main_menu_bg.draw(draw_tools, 0, 0);
}

function draw_button(draw_tools, x, y, text, text_offset_x, w=240, text_offset_y=38, h=50) {
    draw_tools.strokeStyle = "#111";
    draw_tools.strokeRect(x, y, w, h);
    draw_tools.fillStyle = "#AAF";
    draw_tools.fillRect(x, y, w, h);
    draw_text(draw_tools, text, x + text_offset_x, y + text_offset_y);
}
function draw_text(draw_tools, text, x, y, fill_style="#00F", font="italic 30pt Times New Roman") {
    draw_tools.fillStyle = fill_style;
    draw_tools.font = font;
    draw_tools.fillText(text, x, y);
}

function runProgram() {
  /* функция получает canvas из HTML, достаёт из него инструментарий draw_tools
     и передаёт его процедуре рисования */
  canvas_element = document.getElementsByTagName("canvas")[0];
  draw_tools = canvas_element.getContext("2d");
  window.requestAnimationFrame(drawLoop);
  function drawLoop() {
      draw(draw_tools);
      window.requestAnimationFrame(drawLoop);
  }
}

runProgram();






//    draw_text(draw_tools, "Подземелье Джася!", 10, 60, "#F00", "bold 50pt Times New Roman");
//    draw_button(draw_tools, 180, 100, "Поехали!", 40)
//    draw_button(draw_tools, 180, 160, "Загрузить", 30)
//    draw_button(draw_tools, 180, 220, "Достижения", 10)
//    draw_button(draw_tools, 180, 280, "Настройки", 20)
/*
function draw_progress_bar(draw_tools, x, y, w, h, percent) {
    draw_tools.strokeStyle = "#111";
    draw_tools.strokeRect(x, y, w, h);
    draw_tools.fillStyle = "#AAA";
    draw_tools.fillRect(x, y, w, h);
    draw_tools.fillStyle = "#0F0";
    draw_tools.fillRect(x, y, w * percent / 100, h);
}
function draw_storage(draw_tools, x, y, w, h, max, current) {
    var percent = current / max * 100;
    draw_progress_bar(draw_tools, x, y, w, h, percent);
    y += 37
    x += 5
    w += 5
    draw_text(draw_tools, current, x, y)
    draw_tools.strokeText(current, x, y)
    draw_text(draw_tools, "/ " + max, x + w, y)
    draw_tools.strokeText("/ " + max, x + w, y)
}



    button_image = new Image();
    button_image.onload = Function() { draw_tools.drawImage(button_image, button_x, button_y, button_w, button_h); }
    button_image.src = "https://kartinkin.net/uploads/posts/2022-03/1647025979_40-kartinkin-net-p-kartinki-knopki-41.png"
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
