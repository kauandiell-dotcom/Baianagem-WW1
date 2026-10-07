from pathlib import Path

content_pt = """\ufeffl_braz_por:
 ww1_super_event_dispatch_header:0 "§YDESPACHO EXTRAORDINÁRIO§!"
 ww1_super_event_outbreak_title:0 "§R— A GRANDE GUERRA —§!"
 ww1_super_event_outbreak_quote:0 "§O\\\"As lâmpadas estão se apagando por toda a Europa; não as veremos acesas novamente em nosso tempo de vida.\\\"§!\\n§g— Sir Edward Grey, Secretário de Relações Exteriores Britânico, 3 de Agosto de 1914§!"
 ww1_super_event_outbreak_button:0 "§YQue Deus tenha piedade de nossas almas.§!"
 ww1_outbreak.1.t:0 "Tiros em Sarajevo"
 ww1_outbreak.1.d:0 "O arquiduque Francisco Ferdinando e sua esposa Sofia foram assassinados durante a visita a Sarajevo. O herdeiro do trono austro-húngaro havia mantido seus compromissos públicos após uma primeira tentativa contra a comitiva. Um segundo ataque, no Cais Appel, foi fatal.\\n\\nO atirador preso, Gavrilo Princip, pertence ao ambiente revolucionário da Jovem Bósnia. A investigação sobre seus cúmplices apenas começou. Em Viena, autoridades já exigem explicações de Belgrado, enquanto o governo sérvio teme que as acusações se transformem em um ultimato.\\n\\nO luto se espalhou pelas terras dos Habsburgo. A portas fechadas, ministros e estados-maiores avaliam medidas cujas consequências podem ultrapassar os Bálcãs."
 ww1_outbreak.1.a:0 "O império precisa descobrir quem está por trás disso."
 ww1_outbreak.1.b:0 "Nossa resposta deve proteger a Sérvia da catástrofe."
 ww1_outbreak.1.c:0 "A diplomacia enfrenta sua prova mais difícil."
 ww1_outbreak.2.t:0 "Guerra Geral na Europa"
 ww1_outbreak.2.d:0 "As trocas diplomáticas deram lugar a ordens de mobilização. Ferrovias levam reservistas às fronteiras, portos se preparam para o tráfego de guerra e governos pedem que seus cidadãos aceitem sacrifícios cuja duração ninguém pode prever honestamente.\\n\\nO conflito arrastou as grandes potências para campos opostos. Cada declaração altera os cálculos dos países ainda fora dos combates. Alianças, rotas comerciais e a segurança de territórios distantes passam a integrar a mesma guerra.\\n\\nMultidões celebram a partida dos regimentos. Suas famílias aguardam cartas. O resultado dependerá de exércitos e fábricas, transportes e diplomacia, e da resistência de sociedades que ainda descobrirão o preço de uma guerra moderna."
 ww1_outbreak.2.a:0 "Precisamos conduzir nosso povo através desta guerra."
 ww1_outbreak.2.b:0 "A neutralidade exigirá vigilância."
 ww1_great_war_dispatch:0 "A Grande Guerra — Despacho Extraordinário"
"""

content_en = """\ufeffl_english:
 ww1_super_event_dispatch_header:0 "§YEXTRAORDINARY DISPATCH§!"
 ww1_super_event_outbreak_title:0 "§R— THE GREAT WAR —§!"
 ww1_super_event_outbreak_quote:0 "§O\\\"The lamps are going out all over Europe; we shall not see them lit again in our lifetime.\\\"§!\\n§g— Sir Edward Grey, British Foreign Secretary, 3 August 1914§!"
 ww1_super_event_outbreak_button:0 "§YMay God have mercy upon our souls.§!"
 ww1_outbreak.1.t:0 "Shots in Sarajevo"
 ww1_outbreak.1.d:0 "Archduke Franz Ferdinand and his wife Sophie have been assassinated during their visit to Sarajevo. The heir to the Austro-Hungarian throne had continued his public schedule following an earlier attempt against his motorcade. A second attack on the Appel Quay proved fatal.\\n\\nThe captured gunman, Gavrilo Princip, belongs to the revolutionary Young Bosnia movement. The investigation into his accomplices has only begun. In Vienna, officials already demand explanations from Belgrade, while the Serbian government fears the accusations will escalate into an ultimatum.\\n\\nMourning spreads across the Habsburg lands. Behind closed doors, ministers and general staffs weigh measures whose consequences may reach far beyond the Balkans."
 ww1_outbreak.1.a:0 "The Empire must discover who stands behind this."
 ww1_outbreak.1.b:0 "Our answer must shield Serbia from ruin."
 ww1_outbreak.1.c:0 "Diplomacy faces its sternest trial."
 ww1_outbreak.2.t:0 "General War in Europe"
 ww1_outbreak.2.d:0 "Diplomatic exchanges have yielded to mobilization orders. Railways carry reservists to borders, ports prepare for wartime traffic, and governments ask their citizens to shoulder sacrifices whose duration no one can honestly predict.\\n\\nThe conflict has swept the great powers into opposing camps. Every declaration shifts the calculations of nations still outside the fighting. Treaties, trade routes, and distant overseas territories now belong to the same war.\\n\\nCrowds cheer departing regiments. Their families await letters. The outcome will turn on armies and factories, transport and statecraft, and the stamina of societies only beginning to learn the true cost of modern war."
 ww1_outbreak.2.a:0 "We must guide our people through this war."
 ww1_outbreak.2.b:0 "Neutrality will require vigilance."
 ww1_great_war_dispatch:0 "The Great War — Extraordinary Dispatch"
"""

Path('localisation/braz_por/ww1_super_events_l_braz_por.yml').write_bytes(content_pt.encode('utf-8'))
Path('localisation/english/ww1_super_events_l_english.yml').write_bytes(content_en.encode('utf-8'))
print('Super events loc updated successfully with UTF-8 BOM!')
