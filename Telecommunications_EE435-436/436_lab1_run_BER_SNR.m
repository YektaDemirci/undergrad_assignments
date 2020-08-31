iter=0;
barker5_ex = [1 1 1   1 1 1    1 1 1   -1 -1 -1  1 1 1];
barker5_fin=[zeros(1,12)  fliplr(barker5_ex) zeros(1,12) ];

barker7_ex = [1 1 1   1 1 1    1 1 1   -1 -1 -1  -1 -1 -1  1 1 1  -1 -1 -1];
barker7_fin=[zeros(1,9)  fliplr(barker7_ex) zeros(1,9) ];

barker11_ex = [1 1 1   1 1 1    1 1 1   -1 -1 -1  -1 -1 -1 -1 -1 -1  1 1 1  -1 -1 -1 -1 -1 -1 1 1 1 -1 -1 -1];
barker11_fin=[zeros(1,3)  fliplr(barker11_ex) zeros(1,3) ];


own_coeff=barker11_fin;
own_coeff_even=own_coeff(2: 2: end);
own_coeff_odd=own_coeff(1: 2: end);

for noise_var=[ 0 ]%0.075 0.085 0.1 0.2 0.4]
    
%     for noise_var=[ 0.2 0.4]
    iter=iter+1;
    simOut = sim('rtlsdr_QPSK_ascii_message_lab1','StopTime', '30')
    no_of_bit_err=sum(simOut.get('simout_no_of_err').Data(80:end));            % Total number of bit errors. We omit the first 80 realization since the synchronization blocks may not have synchronized well to the received signal.
    total_no_of_bits=length(simOut.get('simout_no_of_err').Data(80:end))*8*12; % Multiplication by 12 is due to the fact that Hello World! string has 12 character and each character is represented by 8 bits.
    % Write the single line code to find BER rate
    BER(iter)=no_of_bit_err / total_no_of_bits;
    
    input_symbols_to_AWGN_block=simOut.get('signal_before_awgn').Data(80:end); % Signal before AWGN block, from the "To workspace" block connected to "AWGN channel" block input.
    output_symbols_AWGN_block=simOut.get('signal_after_awgn').Data(80:end);    % Signal after AWGN block, from the "To workspace" block connected to "AWGN channel" block input.
    
    % Select the symbols in one of the quadrants in the constellation. Here, the first quadrant symbols are selected.
    first_quadrant_symbols=input_symbols_to_AWGN_block(abs((real(input_symbols_to_AWGN_block)-0.707))<0.707 & abs((imag(input_symbols_to_AWGN_block)-0.707))<0.707);
    
    % Find the signal power
    Psig = mean(abs(first_quadrant_symbols).^2);
    
    % Find the noise power
    Pout = mean(abs(output_symbols_AWGN_block).^2);
    Pnoise = Pout - Psig;
    
    % Calculate SNR in dB
    SNR = 20*log10(Psig/Pnoise);
    
    observed_SNR(iter)=SNR;

end

EbNo=0:10;
figure;
theoretical_ber_qdpsk=berawgn(EbNo,'dpsk',4);       % Take theoretical values for BER of QDPSK
semilogy(EbNo,theoretical_ber_qdpsk,'linewidth',2)  % Plot Theoretical QDPSK BER
hold on
semilogy(observed_SNR-3,BER,'linewidth',2);         % Plot the QDPSK BER we observe empirically (-3 dB is due to conversion from symbol to bit SNR)
legend('Theoretical BER QDPSK','Empirical BER QDPSK')
grid on