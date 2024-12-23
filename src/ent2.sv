module ent2 (
    input  logic c,
    output logic d
);
    ent ent_inst (
        .a(c),
        .b(d)
    );

endmodule
