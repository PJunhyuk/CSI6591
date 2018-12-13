clc;
clear;

[music_acp, Fs] = audioread('acappella_hash.mp3');
music_acp_l = music_acp(:, 1);

% player = audioplayer(music_acp_l, Fs);
% play(player);

% [d, sr] = audioread('acappella_hash.wav');
% b = beat(d(:,1), sr);

