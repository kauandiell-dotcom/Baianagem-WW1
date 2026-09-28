---
name: hoi4-scripting
description: Guia de boas práticas de scripting no Clausewitz Engine para HOI4 1.19.3. Scopes, triggers, effects e armadilhas comuns.
---

# Skill: Scripting para Hearts of Iron IV (v1.19.3)

Esta skill estabelece a referência técnica para escrita de scripts na versão estável alvo do mod.

## 1. Escopos Fundamentais (Scopes)
- `ROOT`: O país ou estado que originou a ação (geralmente quem tomou a decisão, disparou o evento ou selecionou o foco).
- `FROM`: O país ou entidade remetente quando um evento é enviado de um país para outro.
- `PREV`: O escopo imediatamente anterior na pilha de avaliação de blocos aninhados.
- `THIS`: O escopo atual em avaliação.

## 2. Modifiers Críticos
- Sempre usar `consumer_goods_expected_value = 0.05` para acréscimo de 5% de bens de consumo, ou `-0.05` para redução de 5%. Não usar o deprecated `consumer_goods_factor`.
- Para indústrias: `production_speed_industrial_complex_factor`, `production_speed_arms_factory_factor`.
- Para estabilidade e suporte de guerra: `stability_factor` / `stability_weekly` e `war_support_factor` / `war_support_weekly`.

## 3. Scripted Effects e Scripted Triggers
- Definir em `common/scripted_effects/` ou `common/scripted_triggers/`.
- Permitem passagem de parâmetros e eliminação de duplicação massiva de código.
- Exemplo de sintaxe:
```text
# common/scripted_effects/ww1_effects.txt
ww1_apply_trench_attrition = {
    add_state_modifier = {
        modifier = ww1_heavy_mud_modifier
        days = 30
    }
}
```

## 4. Cuidados com Variáveis
- Variáveis globais vs locais de país:
  - `set_variable = { var_name = 10 }` (no escopo do país)
  - `set_variable = { global.var_name = 10 }` (global)
- Comparação:
  - `check_variable = { var_name > 5 }`
