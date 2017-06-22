/*
 * 这是一张 JavaScript 代码草稿纸。
 *
 * 输入一些 JavaScript，然后可点击右键或从“执行”菜单中选择：
 * 1. 运行 对选中的文本求值(eval) (Ctrl+R)；
 * 2. 查看 对返回值使用对象查看器 (Ctrl+I)；
 * 3. 显示 在选中内容后面以注释的形式插入返回的结果。 (Ctrl+L)
 */

String.prototype.print_f = function() {
    var formatted = this;
    for (var i = 0; i < arguments.length; i++) {
        var regexp = new RegExp('\\{'+i+'\\}', 'gi');
        formatted = formatted.replace(regexp, arguments[i]);
    }
    return formatted;
};
/*获取表格内行和列的内容*/
var tr = document.getElementsByTagName('tr');
var td = document.getElementsByTagName('td');
var th = document.getElementsByTagName('th');
var arr_list = document.getElementById('arr_list');
console.log(tr);
console.log(td);
console.log(th);
/*新建一个二维数组*/
var depData = {};
var height = 0;
var age = 0;
var tdnum = 10;
for (var l = 1; l < th.length; l++) {
  age = th[l].innerText;
  depData[age] = {};
  for (var k = 1; k < tr[0].children.length; k++) {
    height = tr[0].children[k].innerText;
    depData[age][height] = td[tdnum].innerText;
    tdnum++;
  }
}
console.log(depData);

arr_list.innerHTML = depData.toSource();