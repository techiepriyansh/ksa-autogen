module grey_cell(pg_a, g_b, g_out);

//pg_a = i:k
//g_b = k-1:j only generate
//g_out = i:k only generate

//propagate = pg[1]
//generate = pg[0]

input [1:0] pg_a;
input g_b;

output g_out;

wire tmp;

and(tmp, pg_a[1], g_b);
or(g_out, pg_a[0], tmp);

endmodule