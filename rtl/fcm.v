module fcm (
    input wire clk,
    input wire reset,
    input wire [3:0] input_signal
);
    // For demo: drive nothing, just log
    always @(posedge clk) begin
        if (!reset)
            $display("input_signal = %b", input_signal);
    end
endmodule

