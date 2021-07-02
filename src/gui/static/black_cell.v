module black_cell(pg_a, pg_b, pg_out);

//pg_a = i:k
//pg_b = k-1:j
//pg_out = i:k

//propagate = pg[1]
//generate = pg[0]

input [1:0] pg_a, pg_b;
output [1:0] pg_out;

wire tmp;

and(tmp, pg_a[1], pg_b[0]);
or(pg_out[0], pg_a[0], tmp);

and(pg_out[1], pg_a[1], pg_b[1]);

endmodule