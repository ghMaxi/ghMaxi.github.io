var canvas_element = document.getElementsByTagName("canvas")[0];
var canvas_rect = canvas_element.getBoundingClientRect();
var draw_tools = canvas_element.getContext("2d");

function Test(a, b) { this.a = a; this.b = b; this.c="qq2"; }
Test.prototype.c = 'qq';
test = new Test('aa', 'bb');
console.log(test.a+" "+test.b+" "+test.c)

function Rect(x, y, w, h) {
    // конструктор объекта Rect - координаты (x, y) и размеры (w, h)
    this.x = x;
    this.y = y;
    this.w = w;
    this.h = h;
}

Rect.prototype.collide_point = function(point) {
    // проверка что пара координат (point) оказывается внутри Rect
    return ((point[0] > this.x && point[0] < this.x + this.w) &&
            (point[1] > this.y && point[1] < this.y + this.h))
}

function load_image(url) {
    // функция загружает картинку с заданного адреса и возвращает ссылку на неё
    new_image = new Image();
    new_image.src = url;
    return new_image;
}
var menu_bg = load_image("./images/main_menu_bg.jpg");
var button = load_image("./images/button.jpg");
var title_bg = load_image("./images/main_bg.jpg");

function getRandomInt(max) {
    // Функция вовзращает случайное целое число от 0 меньше max
    return Math.floor(Math.random() * max);
}

function boxRandomPixel() {
    // Функция выделяет квадратиком случайный пиксель на canvas_element
    var x = getRandomInt(canvas_element.width);
    var y = getRandomInt(canvas_element.height);
    draw_tools.strokeRect(x-1, y-1, 3, 3);
}

function draw_text(x, y, text, fill_style="#00F", font="italic 30pt Times New Roman") {
    // Функция рисует текст в заданных координатах, с возможностью дополнительно
    // указать fill_style и font
    draw_tools.fillStyle = fill_style;
    draw_tools.font = font;
    draw_tools.fillText(text, x, y);
}

function draw_button(x, y, text, text_offset_x=10, w=240, text_offset_y=38, h=50) {
    // Функция рисует кнопку в заданных координатах с заданным текстом,
    // с возможностью дополнительно ширину кнопки и выравнивание текста внутри
    draw_tools.strokeStyle = "#111";
    draw_tools.strokeRect(x, y, w, h);
    draw_tools.fillStyle = "#AAF";
    draw_tools.fillRect(x, y, w, h);
    draw_text(x + text_offset_x, y + text_offset_y, text);
}

function draw_image(image, x, y, width, height) {
    // функция рисует загруженные картинки и обрабатывает загрузку незагруженных
    if (image.complete && image.naturalHeight !== 0) {
        draw_tools.drawImage(image, x, y, width, height);
    } else {
        draw_tools.strokeStyle = "#111";
        draw_tools.strokeRect(x, y, width, height);
        draw_tools.fillStyle = "#AAF";
        draw_tools.fillRect(x, y, width, height);
        draw_text(x +  width/2 - 15, y + height/2 + 15, "x");
        image.addEventListener('load', draw, false);
    }
}

function draw() {
    // Функция рисует задний план, заголовок и кнопки
    draw_image(menu_bg, 0, 0, canvas_element.width, canvas_element.height);
    draw_image(title_bg, 10, 5, canvas_element.width-20, 80);
    draw_text(10, 60, "Подземелье Джася!", "#F00", "bold 50pt Times New Roman");
    draw_button(180, 100, "Поехали!", 40)
    draw_button(180, 160, "Загрузить", 30)
    draw_button(180, 220, "Достижения", 10)
    draw_button(180, 280, "Настройки", 20)
}

function get_mouse_position(event) {
    // функция получает из MouseEvent координаты клика с точки зрения canvas
    return [event.clientX - canvas_rect.left, event.clientY - canvas_rect.top];
}

function on_mouse_down(event) {
    // функция обрабатывает нажатии кнопки мыши внутри canvas
    test_rect = new Rect(180, 100, 240, 50);
    console.log(test_rect.collide_point(get_mouse_position(event)))
}

function on_key_up(event) {
    // функция обрабатывает отпускание клавиши в окне браузера
    if (event.code == 'Enter') { console.log("enter"); }
}

function on_mouse_move(event) {
    // функция обрабатывает движении мыши внутри canvas
}

function on_mouse_up(event) {
    // функция обрабатывает отпускание кнопки мыши внутри canvas
}

document.addEventListener('keyup', on_key_up);
canvas_element.addEventListener('mousemove', on_mouse_move);
canvas_element.addEventListener('mouseup', on_mouse_up);
canvas_element.addEventListener('mousedown', on_mouse_down);

function run() {
    // функция вызывает отрисовку приложения
    draw();
}


run();






/*function load_image(src) {
    image = new Image();
    image.src = src;
    return image;
}
main_menu_bg = load_image("./images/main_menu_bg.jpg");
button_atlas = load_image("./images/butons.jpg")

LoadedImage.prototype.draw = function(draw_tools, x, y) {
    if (this.image.complete && this.image.naturalHeight > 0) {
        draw_tools.drawImage(this.image, x, y, this.width, this.height);
    } else {
        draw_button(draw_tools, x, y, ":(", this.width/2 - 15, this.width, this.height / 2 + 10, this.height)
    }
}


function draw(draw_tools) {
    main_menu_bg.draw(draw_tools, 0, 0);
}



function runProgram() {
  /* функция получает canvas из HTML, достаёт из него инструментарий draw_tools
     и передаёт его процедуре рисования
  window.requestAnimationFrame(drawLoop);
  function drawLoop() {
      draw(draw_tools);
      window.requestAnimationFrame(drawLoop);
  }
}

runProgram();*/






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
