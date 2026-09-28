---
name: hoi4-events-decisions
description: Criação de eventos de país, notícias e decisões dinâmicas com controle de namespaces e escopos válidos.
---

# Skill: Eventos e Decisões para HOI4

Esta skill define as normas para criação de eventos e sistemas de decisão no mod.

## 1. Organização de Eventos
- **Declaração Obrigatória de Namespace**:
  - Todo arquivo em `events/` deve abrir com `add_namespace = <nome_curto>` (ex.: `add_namespace = ww1_germany`).
  - IDs devem ser sequenciais e legíveis: `ww1_germany.1`, `ww1_germany.2`, etc.
- **Estrutura de Evento**:
```text
country_event = {
    id = ww1_germany.1
    title = ww1_germany.1.t
    desc = ww1_germany.1.d
    picture = GFX_report_event_ww1_mobilization

    is_triggered_only = yes  # Preferencial para performance!

    option = {
        name = ww1_germany.1.a
        ai_chance = { base = 90 }
        # Efeitos
    }
    option = {
        name = ww1_germany.1.b
        ai_chance = { base = 10 }
        # Efeitos alternativos
    }
}
```

## 2. Decisões e Categorias
- Cada decisão deve pertencer a uma categoria registrada em `common/decisions/categories/`.
- Usar `visible = { ... }` para não poluir a interface do jogador com decisões irrelevantes.
- Usar `available = { ... }` para condições de ativação.
- Sempre especificar `ai_will_do = { factor = ... }` para calibrar o uso pela IA.
- Definir `days_re_enable = X` ou `fire_only_once = yes` para prevenir spam.
