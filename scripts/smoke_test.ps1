# scripts/smoke_test.ps1
# SMOKE TEST script for RAG setup

Write-Host "SMOKE TEST..." -ForegroundColor Cyan

# Requires: server running on localhost:8000 and X-API-Key set in .env
$envText = Get-Content .\.env -Raw
$apiKey = ($envText | Select-String -Pattern "^RAG_API_KEY=(.+)$").Matches[0].Groups[1].Value

# Test /health endpoint
$health = Invoke-RestMethod -Uri "http://127.0.0.1:8000/health" -Method GET
Write-Host "health:" ($health | ConvertTo-Json -Compress)

# Test /ask endpoint
$headers = @{ "X-API-Key" = $apiKey }
$body = @{ question = "What is this service?" } | ConvertTo-Json

# Send request to /ask
$ask = Invoke-RestMethod -Uri "http://127.0.0.1:8000/ask" -Method POST -Headers $headers -ContentType "application/json" -Body $body
Write-Host "ask:" ($ask | ConvertTo-Json -Depth 5)
Write-Host "PASS" -ForegroundColor Green
