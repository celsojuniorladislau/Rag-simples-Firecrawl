import streamlit as st
import os
from service.scraping import ScrapingService

def show():
    st.header("🔍Web Scraping")
    
    scraper = ScrapingService()
    
    with st.form("scraping_form"):
        url = st.text_input("URL to site:", placeholder="https://example.com")
        collection_name = st.text_input("Nome da coleção:", placeholder="minha-coleção")
        sudmitted = st.form_submit_button("Iniciar Scraping")
        
        if sudmitted and url and collection_name:
            with st.spinner("Extraindo conteúdo..."):
                result = scraper.scrape_website(url, collection_name)
                
                if result["success"]:
                    st.success(f"✅ Conteúdo extraído com sucesso! {result['files']} arquivos salvos.")
                else:
                    st.error("❌ Erro ao extrair conteúdo. {result['error']}.")
                    
            
         