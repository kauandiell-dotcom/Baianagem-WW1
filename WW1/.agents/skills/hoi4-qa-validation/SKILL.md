---
name: hoi4-qa-validation
description: Métodos automáticos e procedimentos de checagem para balanceamento de chaves, integridade referencial, sprites e codificação UTF-8 BOM.
---

# Skill: Garantia de Qualidade e Validação Automática

Esta skill detalha os scripts e verificações que o agente de QA e a equipe de desenvolvimento devem executar antes de integrar qualquer alteração.

## 1. Verificação de Balanceamento de Chaves (Bracket Balance)
Todo arquivo de script Paradox deve manter a contagem de `{` estritamente igual à contagem de `}`, desconsiderando comentários iniciados por `#` e strings entre aspas.
- Script de verificação rápida em PowerShell:
```powershell
Get-ChildItem -Path <alvo> -Filter *.txt | ForEach-Object {
    $text = [System.IO.File]::ReadAllText($_.FullName)
    $open = 0; $inQuote = $false; $inComment = $false
    for ($i = 0; $i -lt $text.Length; $i++) {
        $c = $text[$i]
        if ($inComment) { if ($c -eq "`n") { $inComment = $false }; continue }
        if ($c -eq '#') { $inComment = $true; continue }
        if ($c -eq '"') { $inQuote = -not $inQuote; continue }
        if (-not $inQuote) {
            if ($c -eq '{') { $open++ }
            elseif ($c -eq '}') { $open-- }
        }
    }
    if ($open -ne 0) { Write-Host "ERRO em $($_.Name): saldo de chaves = $open" -ForegroundColor Red }
}
```

## 2. Verificação de Localização (UTF-8 BOM)
- Todo `.yml` deve começar com os bytes `0xEF, 0xBB, 0xBF`.
- Deve começar na primeira linha com a chave de idioma (ex.: `l_english:`).

## 3. Checagem de Sprites Faltantes
- Identificar todas as chamadas de `picture = "..."` ou `icon = "..."` no código.
- Garantir que cada uma exista em um bloco `spriteType` nos arquivos `interface/*.gfx`.
- Garantir que a textura correspondente exista no disco no caminho declarado.
