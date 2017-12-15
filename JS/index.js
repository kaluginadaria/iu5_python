$(function(){
    var from = $('#from');
    var to = $('#to');
    var func = $('#func');
    var btn = $('#plot_btn');
    var plot = $('#plot');

    btn.click(function(e){
        e.preventDefault();

        var from_val = parseFloat(from.val());
        var to_val = parseFloat(to.val());

        setInterval(function(){
            from_val += 0.1;
            to_val += 0.1;
            var values = []

            for(var x = from_val; x <= to_val; x += 0.1){
                values.push([x, eval(func.val())])
            }

            $.plot(plot, [values], {})
        }, 20);

    });
})