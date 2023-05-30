def is_cep_valid(ceps):
    results = []
    
    for cep in ceps:

        # Removing not a number
        cep = "".join(filter(str.isdigit, cep))
        
        # The cep follows the necessary algorithm?
        if len(cep) != 8:
            results.append(f"{cep}: {None}")
            continue
    
        # Validating CEP
        url = f"https://viacep.com.br/ws/{cep}/json/"
        response = requests.get(url)

        if response.status_code == 400:
            print('')
        
        if response.status_code == 200:
            data = response.json()
            
            if "erro" not in data:
                cidade = data["localidade"]
                results.append(f"{cep}: {cidade}")
            else:
                results.append(f"{cep}: {None}")
        else:
            results.append(f"{cep}: {None}")
    
    return results
