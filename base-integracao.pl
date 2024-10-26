% "Fatos dos pacientes e seus sintomas"
paciente(maria).
paciente(joao).
paciente(ana).
paciente(carlos).

% "Maria, sintomas de (gripe)"
sintoma(maria, febre).
sintoma(maria, dor_de_cabeca).
sintoma(maria, dor_de_garganta).

% "Joao, sintomas de (tose_comum)"
sintoma(joao, dor_de_cabeca).
sintoma(joao, tosse).

% "Ana, n�o possui sintomas claros para uma avalia��o. (FALSE)"
sintoma(ana, espirros).
sintoma(ana, nariz_entupido).

% "Carlos, sintomas de (resfriado)"
sintoma(carlos, espirros).
sintoma(carlos, nariz_entupido).
sintoma(carlos, dor_de_cabeca).

% "Fatos das doen�as e seus sintomas"
doenca(resfriado, [espirros, nariz_entupido, dor_de_cabeca]).
doenca(gripe, [febre, dor_de_cabeca, dor_de_garganta]).
doenca(amigdalite, [dor_de_garganta, febre]).
doenca(tosse_comum, [tosse, dor_de_cabeca]).

% "Regra para verificar as poss�veis doen�as de um paciente com base nos sintomas"
%
% "Em caso de sintomas baterem com a base de avalia��o, retorna a
% possivel doenca."
possivel_doenca(Paciente, Doenca) :-
    paciente(Paciente),
    doenca(Doenca, Sintomas),
    forall(member(Sintoma, Sintomas), sintoma(Paciente, Sintoma)).
