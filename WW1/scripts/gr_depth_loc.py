"""Textos que faltavam nos eventos de 'profundidade' (side_ww1_ger_rus): sem eles o jogador via chaves cruas."""
from gr_lib import loc

S = 'side_ww1_ger_rus.'
TEXTS = {
    '50': (('An Invitation to the Red Internationale', 'Um Convite para a Internacional Vermelha'),
           ('Revolutionary Germany proposes that the two socialist republics join in a single bloc against the capitalist powers. Our comrades in Berlin want an answer.',
            'A Alemanha revolucionária propõe que as duas repúblicas socialistas se unam em um único bloco contra as potências capitalistas. Os camaradas de Berlim esperam uma resposta.'),
           ('Join the Red Internationale.', 'Ingressar na Internacional Vermelha.'), ('Decline for now.', 'Recusar por ora.')),
    '51': (('An Invitation to the Continental League', 'Um Convite para a Liga Continental'),
           ('Berlin proposes a continental league of the great monarchies against the maritime powers. A Russian signature would seal the agreement that Björkö once promised.',
            'Berlim propõe uma liga continental das grandes monarquias contra as potências marítimas. Uma assinatura russa selaria o acordo que Björkö um dia prometeu.'),
           ('Join the Continental League.', 'Ingressar na Liga Continental.'), ('Decline for now.', 'Recusar por ora.')),
    '52': (('Russia Joins Our Bloc', 'A Rússia Ingressa em Nosso Bloco'),
           ('The Russian government has accepted our invitation and takes its place beside us. The Entente powers have been told to expect a new balance in Europe.',
            'O governo russo aceitou nosso convite e toma seu lugar ao nosso lado. As potências da Entente foram avisadas de que devem esperar um novo equilíbrio na Europa.'),
           ('A great diplomatic success.', 'Um grande sucesso diplomático.')),
    '55': (('Russia Declines Our Bloc', 'A Rússia Recusa Nosso Bloco'),
           ('St Petersburg has politely declined to join our bloc. The door is not closed, but the moment has passed.',
            'São Petersburgo recusou educadamente ingressar em nosso bloco. A porta não está fechada, mas o momento passou.'),
           ('We shall try again.', 'Tentaremos novamente.')),
    '56': (('Bulgaria Joins the Central Powers', 'A Bulgária Ingressa nas Potências Centrais'),
           ('Sofia has accepted the German proposal and signs the alliance. Bulgarian armies will march with ours in the Balkans.',
            'Sófia aceitou a proposta alemã e assina a aliança. Os exércitos búlgaros marcharão conosco nos Bálcãs.'),
           ('Welcome, ally.', 'Bem-vindo, aliado.')),
    '57': (('Bulgaria Declines', 'A Bulgária Recusa'),
           ('Sofia has declined to tie its fate to ours. The Balkan railway remains open, but Bulgarian soldiers will not wear our colours yet.',
            'Sófia recusou atrelar seu destino ao nosso. A ferrovia balcânica continua aberta, mas os soldados búlgaros ainda não vestirão nossas cores.'),
           ('A pity.', 'Uma pena.')),
    '60': (('Germany Proposes Union', 'A Alemanha Propõe a União'),
           ('With the Habsburg monarchy gone, Berlin offers the Austrian republic union with Germany. Vienna is poor, hungry and divided on the answer.',
            'Com a monarquia dos Habsburgo extinta, Berlim oferece à república austríaca a união com a Alemanha. Viena é pobre, faminta e dividida quanto à resposta.'),
           ('Accept the union with Germany.', 'Aceitar a união com a Alemanha.'), ('Decline the offer.', 'Recusar a oferta.')),
    '61': (('Austria Joins the Reich', 'A Áustria Ingressa no Reich'),
           ('The Austrian republic has accepted the union. German officials arrive in Vienna to begin the long work of integration.',
            'A república austríaca aceitou a união. Funcionários alemães chegam a Viena para iniciar o longo trabalho de integração.'),
           ('One people, one state.', 'Um povo, um Estado.')),
    '62': (('Austria Declines Union', 'A Áustria Recusa a União'),
           ('Vienna has turned down our offer of union. The Entente had made its views known, and the Austrian parties chose caution.',
            'Viena recusou nossa oferta de união. A Entente deixou claras suas opiniões, e os partidos austríacos optaram pela cautela.'),
           ('Perhaps another day.', 'Talvez em outro dia.')),
}
for num, spec in TEXTS.items():
    t, d, *opts = spec
    loc(S + num + '.t', *t)
    loc(S + num + '.d', *d)
    for k, (en, pt) in enumerate(opts):
        loc(S + num + '.' + 'ab'[k], en, pt)
