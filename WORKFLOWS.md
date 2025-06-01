# n8n Workflows Collection

A comprehensive catalog of n8n workflow automation templates organized by business function and category.

## 📊 Collection Overview

- **Total Workflows**: 2,050
- **Categories**: 10
- **Integration Patterns**: 335

### Category Distribution

| Category | Count | Description |
|----------|-------|-------------|
| AI | 896 | AI-powered workflows for automation, analysis, and intelligent processing |
| UTIL | 512 | Utility workflows for general automation and system operations |
| COMM | 281 | Communication workflows for messaging, notifications, and team collaboration |
| DATA | 204 | Data processing, transformation, and management workflows |
| BIZ | 60 | Business process automation and workflow management |
| CONTENT | 37 | Content creation, publishing, and management workflows |
| OPS | 34 | Operations and infrastructure management workflows |
| ECOMMERCE | 13 | E-commerce and online store automation workflows |
| ANALYTICS | 12 | Analytics, reporting, and business intelligence workflows |
| MARKETING | 1 | Marketing automation and campaign management workflows |

### Most Popular Integrations

| Integration | Usage Count | Type |
|-------------|-------------|------|
| httprequest | 775 | HTTP/API |
| manual | 485 | Manual Trigger |
| webhook | 221 | Webhook |
| splitinbatches | 205 | Service |
| gmail | 186 | Email |
| n8n-nodes-langchain.memorybufferwindow | 179 | Service |
| schedule | 172 | Scheduling |
| n8n-nodes-langchain.chainllm | 171 | Service |
| n8n-nodes-langchain.outputparserstructured | 143 | Service |
| n8n-nodes-langchain.chat | 140 | Service |
| slack | 134 | Communication |
| telegram | 123 | Messaging |
| n8n-nodes-langchain.lmchatopenai | 113 | Service |
| googlesheets | 101 | Spreadsheet |
| cron | 75 | Scheduling |

## 📑 Quick Navigation

- [AI](#ai) (896 workflows)
- [UTIL](#util) (512 workflows)
- [COMM](#comm) (281 workflows)
- [DATA](#data) (204 workflows)
- [BIZ](#biz) (60 workflows)
- [CONTENT](#content) (37 workflows)
- [OPS](#ops) (34 workflows)
- [ECOMMERCE](#ecommerce) (13 workflows)
- [ANALYTICS](#analytics) (12 workflows)
- [MARKETING](#marketing) (1 workflows)

## AI

*896 workflows in this category*

| Workflow Name | Business Function | Key Integrations | Complexity | File |
|---------------|-------------------|------------------|------------|------|
| #️⃣Nostr #damus AI Powered Reporting + Gmail + Telegram | ai_process | n8n-nodes-langchain.chainllm, gmail, markdown | 🔴 High | [02GdRzvsuHmSSgBw_#️⃣Nostr_#damus_AI_Powered_Reporting_+_Gmail_+_Telegram.json](workflows/02GdRzvsuHmSSgBw_#️⃣Nostr_#damus_AI_Powered_Reporting_+_Gmail_+_Telegram.json) |
| (G) - Email Classification | ai_process | gmail, gmail, n8n-nodes-langchain.textclassifier | 🔴 High | [m8gr0YZgCx5Qrsia_(G)_-_Email_Classification.json](workflows/m8gr0YZgCx5Qrsia_(G)_-_Email_Classification.json) |
| AI Agent - Cv Resume - Automated Screening , Sorting , Rating and Tracker System | ai_process | n8n-nodes-langchain.lmchatgroq, googlesheets, googledocs | 🔴 High | [2ddwHvuidKc6lZia_AI_Agent_-_Cv_Resume_-_Automated_Screening_,_Sorting_,_Rating_and_Tracker_System.json](workflows/2ddwHvuidKc6lZia_AI_Agent_-_Cv_Resume_-_Automated_Screening_,_Sorting_,_Rating_and_Tracker_System.json) |
| AI Agent : Google calendar assistant using OpenAI | ai_process | n8n-nodes-langchain.memorybufferwindow, n8n-nodes-langchain.chat, googlecalendar | 🟡 Medium | [AI Agent _ Google calendar assistant using OpenAI.json](workflows/AI Agent _ Google calendar assistant using OpenAI.json) |
| AI Agent To Chat With Files In Supabase Storage | ai_process | splitinbatches, supabase, n8n-nodes-langchain.vectorstore | 🔴 High | [AI Agent To Chat With Files In Supabase Storage.json](workflows/AI Agent To Chat With Files In Supabase Storage.json) |
| AI Agent for project management and meetings with Airtable and Fireflies | ai_process | httprequest, googlecalendar, webhook | 🔴 High | [AI Agent for project management and meetings with Airtable and Fireflies.json](workflows/AI Agent for project management and meetings with Airtable and Fireflies.json) |
| AI Agent for realtime insights on meetings | ai_process | postgres, supabase, postgres | 🔴 High | [AI Agent for realtime insights on meetings.json](workflows/AI Agent for realtime insights on meetings.json) |
| AI Agent to chat with Supabase_PostgreSQL DB | ai_process | n8n-nodes-langchain.chat, postgres, n8n-nodes-langchain.lmchatopenai | 🟡 Medium | [AI Agent to chat with Supabase_PostgreSQL DB.json](workflows/AI Agent to chat with Supabase_PostgreSQL DB.json) |
| AI Agent to chat with you Search Console Data, using OpenAI and Postgres | ai_process | n8n-nodes-langchain.memorypostgreschat, httprequest, webhook | 🔴 High | [AI Agent to chat with you Search Console Data, using OpenAI and Postgres.json](workflows/AI Agent to chat with you Search Console Data, using OpenAI and Postgres.json) |
| AI Agent to chat with you Search Console Data, using OpenAI and Postgres | ai_process | n8n-nodes-langchain.memorypostgreschat, httprequest, webhook | 🔴 High | [PoiRk5w0xd1ysq4U_AI_Agent_to_chat_with_you_Search_Console_Data,_using_OpenAI_and_Postgres.json](workflows/PoiRk5w0xd1ysq4U_AI_Agent_to_chat_with_you_Search_Console_Data,_using_OpenAI_and_Postgres.json) |
| AI Agent with Ollama for current weather and wiki | ai_process | n8n-nodes-langchain.memorybufferwindow, n8n-nodes-langchain.wikipedia, n8n-nodes-langchain.httprequest | 🟡 Medium | [AI Agent with Ollama for current weather and wiki.json](workflows/AI Agent with Ollama for current weather and wiki.json) |
| AI Agent with charts capabilities using OpenAI Structured Output | ai_process | n8n-nodes-langchain.memorybufferwindow, n8n-nodes-langchain.chat, httprequest | 🟡 Medium | [6yNJxDjV9rSiOkj9_AI_Agent_with_charts_capabilities_using_OpenAI_Structured_Output.json](workflows/6yNJxDjV9rSiOkj9_AI_Agent_with_charts_capabilities_using_OpenAI_Structured_Output.json) |
| AI Automated TikTok/Youtube Shorts/Reels Generator | ai_process | httprequest, schedule, googledrive | 🔴 High | [aqLL3BAXqQIjeJDt_AI_Automated_TikTok_Youtube_Shorts_Reels_Generator.json](workflows/aqLL3BAXqQIjeJDt_AI_Automated_TikTok_Youtube_Shorts_Reels_Generator.json) |
| AI CV Screening Workflow | ai_process | n8n-nodes-langchain.chainllm, gmail, n8n-nodes-langchain.lmchatgooglegemini | 🟡 Medium | [ES4TSw9HacxoNhLZ_AI_CV_Screening_Workflow.json](workflows/ES4TSw9HacxoNhLZ_AI_CV_Screening_Workflow.json) |
| AI CV Screening Workflow | ai_process | n8n-nodes-langchain.chainllm, gmail, n8n-nodes-langchain.lmchatgooglegemini | 🟡 Medium | [Screen Applicants With AI, notify HR and save them in a Google Sheet.json](workflows/Screen Applicants With AI, notify HR and save them in a Google Sheet.json) |
| AI Customer-Support Assistant · WhatsApp Ready · Works for Any Business | ai_process | whatsapp, n8n-nodes-langchain.memorypostgreschat, n8n-nodes-langchain.httprequest | 🔴 High | [J2D0BssoDmn4BC6D_AI_Customer-Support_Assistant_·_WhatsApp_Ready_·_Works_for_Any_Business.json](workflows/J2D0BssoDmn4BC6D_AI_Customer-Support_Assistant_·_WhatsApp_Ready_·_Works_for_Any_Business.json) |
| AI Data Extraction with Dynamic Prompts and Airtable | ai_process | splitinbatches, n8n-nodes-langchain.chainllm, httprequest | 🔴 High | [AI Data Extraction with Dynamic Prompts and Airtable.json](workflows/AI Data Extraction with Dynamic Prompts and Airtable.json) |
| AI Data Extraction with Dynamic Prompts and Baserow | ai_process | splitinbatches, n8n-nodes-langchain.chainllm, httprequest | 🔴 High | [AI Data Extraction with Dynamic Prompts and Baserow.json](workflows/AI Data Extraction with Dynamic Prompts and Baserow.json) |
| AI Document Assistant via Telegram + Supabase | ai_process | telegram, extractfromfile, n8n-nodes-langchain.textsplitterrecursivecharactertextsplitter | 🔴 High | [LL0TBxEbXoK2zhqp_AI_Document_Assistant_via_Telegram_+_Supabase.json](workflows/LL0TBxEbXoK2zhqp_AI_Document_Assistant_via_Telegram_+_Supabase.json) |
| AI Email processing autoresponder with approval (Yes/No) | ai_process | emailsend, n8n-nodes-langchain.chainsummarization, gmail | 🔴 High | [AI-powered email processing autoresponder and response approval (Yes_No).json](workflows/AI-powered email processing autoresponder and response approval (Yes_No).json) |
| AI Email processing autoresponder with approval (Yes/No) | ai_process | emailsend, n8n-nodes-langchain.chainsummarization, gmail | 🔴 High | [OuHrYOR3uWGmrhWQ_AI_Email_processing_autoresponder_with_approval_(Yes_No).json](workflows/OuHrYOR3uWGmrhWQ_AI_Email_processing_autoresponder_with_approval_(Yes_No).json) |
| AI Fitness Coach Strava Data Analysis and Personalized Training Insights | ai_process | gmail, emailsend, n8n-nodes-langchain.lmchatgooglegemini | 🔴 High | [AI Fitness Coach Strava Data Analysis and Personalized Training Insights.json](workflows/AI Fitness Coach Strava Data Analysis and Personalized Training Insights.json) |
| AI Logo Sheet Extractor to Airtable | ai_process | splitinbatches, crypto, n8n-nodes-langchain.outputparserstructured | 🔴 High | [Extract Information from a Logo Sheet using forms, AI, Google Sheet and Airtable.json](workflows/Extract Information from a Logo Sheet using forms, AI, Google Sheet and Airtable.json) |
| AI Logo Sheet Extractor to Airtable | ai_process | splitinbatches, crypto, n8n-nodes-langchain.outputparserstructured | 🔴 High | [dDAqkobn2pqgdl2N_AI_Logo_Sheet_Extractor_to_Airtable.json](workflows/dDAqkobn2pqgdl2N_AI_Logo_Sheet_Extractor_to_Airtable.json) |
| AI Phone Agent with RetellAI | ai_process | n8n-nodes-langchain.outputparserstructured, httprequest, telegram | 🔴 High | [29P4X9mTSmplnjlJ_AI_Phone_Agent_with_RetellAI.json](workflows/29P4X9mTSmplnjlJ_AI_Phone_Agent_with_RetellAI.json) |
| AI Powered Web Scraping with Jina, Google Sheets and OpenAI _ the EASY way | ai_process | httprequest, n8n-nodes-langchain.lmchatopenai, n8n-nodes-langchain.informationextractor | 🟡 Medium | [AI Powered Web Scraping with Jina, Google Sheets and OpenAI _ the EASY way.json](workflows/AI Powered Web Scraping with Jina, Google Sheets and OpenAI _ the EASY way.json) |
| AI Social Media Caption Creator | ai_process | n8n-nodes-langchain.memorybufferwindow, airtable, n8n-nodes-langchain.lmchatopenai | 🟡 Medium | [V8ypWn7oaOVS3zH0_AI_Social_Media_Caption_Creator.json](workflows/V8ypWn7oaOVS3zH0_AI_Social_Media_Caption_Creator.json) |
| AI Social Media Caption Creator | ai_process | n8n-nodes-langchain.memorybufferwindow, airtable, n8n-nodes-langchain.lmchatopenai | 🟡 Medium | [AI Social Media Caption Creator creates social media post captions in Airtable.json](workflows/AI Social Media Caption Creator creates social media post captions in Airtable.json) |
| AI Social Media Publisher from WordPress | ai_process | wordpress, n8n-nodes-langchain.chainllm, n8n-nodes-langchain.outputparserstructured | 🔴 High | [U9RofpXSIIUg12f9_AI_Social_Media_Publisher_from_WordPress.json](workflows/U9RofpXSIIUg12f9_AI_Social_Media_Publisher_from_WordPress.json) |
| AI T-Shirt Redesign Workflow from any Mockup Image | ai_process | n8n-nodes-langchain.chat, httprequest, n8n-nodes-langchain.lmchatopenai | 🔴 High | [ZpgJpdtmq6MM1jr2_AI_T-Shirt_Redesign_Workflow_from_any_Mockup_Image.json](workflows/ZpgJpdtmq6MM1jr2_AI_T-Shirt_Redesign_Workflow_from_any_Mockup_Image.json) |
| AI Voice Chat using Webhook, Memory Manager, OpenAI, Google Gemini & ElevenLabs | ai_process | n8n-nodes-langchain.memorybufferwindow, n8n-nodes-langchain.chainllm, httprequest | 🔴 High | [AI Voice Chat using Webhook, Memory Manager, OpenAI, Google Gemini & ElevenLabs.json](workflows/AI Voice Chat using Webhook, Memory Manager, OpenAI, Google Gemini & ElevenLabs.json) |
| AI Voice Chat using Webhook, Memory Manager, OpenAI, Google Gemini & ElevenLabs | ai_process | n8n-nodes-langchain.memorybufferwindow, n8n-nodes-langchain.chainllm, httprequest | 🔴 High | [TtoDcjgthgA4NTkU_AI_Voice_Chat_using_Webhook,_Memory_Manager,_OpenAI,_Google_Gemini_&_ElevenLabs.json](workflows/TtoDcjgthgA4NTkU_AI_Voice_Chat_using_Webhook,_Memory_Manager,_OpenAI,_Google_Gemini_&_ElevenLabs.json) |
| AI agent chat | ai_process | n8n-nodes-langchain.memorybufferwindow, n8n-nodes-langchain.chat, n8n-nodes-langchain.lmchatopenai | 🟢 Low | [AI agent chat.json](workflows/AI agent chat.json) |
| AI agent: expense tracker in Google Sheets and n8n chat | ai_process | n8n-nodes-langchain.memorybufferwindow, n8n-nodes-langchain.chat, n8n-nodes-langchain.lmchatopenai | 🟡 Medium | [Simple Expense Tracker with n8n Chat, AI Agent and Google Sheets.json](workflows/Simple Expense Tracker with n8n Chat, AI Agent and Google Sheets.json) |
| AI chat with any data source (using the n8n workflow tool) | ai_process | executeworkflow, n8n-nodes-langchain.manualchat, n8n-nodes-langchain.lmchatopenai | 🔴 High | [AI chat with any data source (using the n8n workflow tool).json](workflows/AI chat with any data source (using the n8n workflow tool).json) |
| AI chatbot that can search the web | ai_process | n8n-nodes-langchain.memorybufferwindow, n8n-nodes-langchain.wikipedia, n8n-nodes-langchain.manualchat | 🟡 Medium | [AI chatbot that can search the web.json](workflows/AI chatbot that can search the web.json) |
| AI powered SEO Keyword Research Automation - The vibe Marketer | ai_process | nocodb, slack, n8n-nodes-langchain.outputparserstructured | 🔴 High | [nGpVbW7RTylKujyT_AI_powered_SEO_Keyword_Research_Automation_-_The_vibe_Marketer.json](workflows/nGpVbW7RTylKujyT_AI_powered_SEO_Keyword_Research_Automation_-_The_vibe_Marketer.json) |
| AI web researcher for sales | ai_process | splitinbatches, n8n-nodes-langchain.outputparserstructured, schedule | 🔴 High | [AI web researcher for sales.json](workflows/AI web researcher for sales.json) |
| AI-Driven Lead Management and Inquiry Automation with ERPNext & n8n | ai_process | N/A | 🟢 Low | [AI-Driven Lead Management and Inquiry Automation with ERPNext & n8n.json](workflows/AI-Driven Lead Management and Inquiry Automation with ERPNext & n8n.json) |
| AI-Driven WooCommerce Product Importer with SEO | ai_process | splitinbatches, woocommerce, n8n-nodes-langchain.chainllm | 🔴 High | [YkATyvsBXigxnMgo_AI-Driven_WooCommerce_Product_Importer_with_SEO.json](workflows/YkATyvsBXigxnMgo_AI-Driven_WooCommerce_Product_Importer_with_SEO.json) |
| AI-Powered Candidate Shortlisting Automation for ERPNext | ai_process | httprequest, microsoftoutlook, erpnext | 🔴 High | [AI-Powered Candidate Shortlisting Automation for ERPNext.json](workflows/AI-Powered Candidate Shortlisting Automation for ERPNext.json) |
| AI-Powered Children_s Arabic Storytelling on Telegram | ai_process | n8n-nodes-langchain.chainsummarization, schedule, n8n-nodes-langchain.lmchatopenai | 🔴 High | [AI-Powered Children_s Arabic Storytelling on Telegram.json](workflows/AI-Powered Children_s Arabic Storytelling on Telegram.json) |
| AI-Powered Children_s English Storytelling on Telegram with OpenAI | ai_process | n8n-nodes-langchain.chainsummarization, schedule, n8n-nodes-langchain.lmchatopenai | 🔴 High | [AI-Powered Children_s English Storytelling on Telegram with OpenAI.json](workflows/AI-Powered Children_s English Storytelling on Telegram with OpenAI.json) |
| AI-Powered Information Monitoring with OpenAI, Google Sheets, Jina AI and Slack | ai_process | slack, n8n-nodes-langchain.chainllm, n8n-nodes-langchain.textclassifier | 🔴 High | [AI-Powered Information Monitoring with OpenAI, Google Sheets, Jina AI and Slack.json](workflows/AI-Powered Information Monitoring with OpenAI, Google Sheets, Jina AI and Slack.json) |
| AI-Powered Information Monitoring with OpenAI, Google Sheets, Jina AI and Slack | ai_process | slack, n8n-nodes-langchain.chainllm, n8n-nodes-langchain.textclassifier | 🔴 High | [Xk0W98z9DVrNHeku_AI-Powered_Information_Monitoring_with_OpenAI,_Google_Sheets,_Jina_AI_and_Slack.json](workflows/Xk0W98z9DVrNHeku_AI-Powered_Information_Monitoring_with_OpenAI,_Google_Sheets,_Jina_AI_and_Slack.json) |
| AI-Powered Research with Jina AI Deep Search | ai_process | n8n-nodes-langchain.chat, httprequest | 🟢 Low | [GToc9QTzJY1h1w3y_AI-Powered_Research_with_Jina_AI_Deep_Search.json](workflows/GToc9QTzJY1h1w3y_AI-Powered_Research_with_Jina_AI_Deep_Search.json) |
| AI-Powered Short-Form Video Generator with OpenAI, Flux, Kling, and ElevenLabs and upload to all social networks | ai_process | writebinaryfile, httprequest, schedule | 🔴 High | [KY0vB3hifSrA24k2_AI-Powered_Short-Form_Video_Generator_with_OpenAI,_Flux,_Kling,_and_ElevenLabs_and_upload_to_all_social_networks.json](workflows/KY0vB3hifSrA24k2_AI-Powered_Short-Form_Video_Generator_with_OpenAI,_Flux,_Kling,_and_ElevenLabs_and_upload_to_all_social_networks.json) |
| AI-Powered WhatsApp Chatbot for Text, Voice, Images & PDFs | ai_process | n8n-nodes-langchain.memorybufferwindow, whatsapp, httprequest | 🔴 High | [zMtPPjJ80JJznrJP_AI-Powered_WhatsApp_Chatbot_for_Text,_Voice,_Images_&_PDFs.json](workflows/zMtPPjJ80JJznrJP_AI-Powered_WhatsApp_Chatbot_for_Text,_Voice,_Images_&_PDFs.json) |
| AI-powered WooCommerce Support-Agent | ai_process | n8n-nodes-langchain.memorybufferwindow, dhl, woocommerce | 🔴 High | [AI-powered WooCommerce Support-Agent.json](workflows/AI-powered WooCommerce Support-Agent.json) |
| Actioning Your Meeting Next Steps using Transcripts and AI | ai_process | n8n-nodes-langchain.outputparserstructured, httprequest, googlecalendar | 🔴 High | [Actioning Your Meeting Next Steps using Transcripts and AI.json](workflows/Actioning Your Meeting Next Steps using Transcripts and AI.json) |
| Add a subscriber to a list and create and send a campaign | ai_process | sendy, manual | 🟢 Low | [14_Add_a_subscriber_to_a_list_and_create_and_send_a_campaign.json](workflows/14_Add_a_subscriber_to_a_list_and_create_and_send_a_campaign.json) |
| Add new incoming emails to a Google Sheets spreadsheet as a new row. | ai_process | gmail, googlesheets | 🟢 Low | [dCLvOuZgc8tToQwu_Add_new_incoming_emails_to_a_Google_Sheets_spreadsheet_as_a_new_row..json](workflows/dCLvOuZgc8tToQwu_Add_new_incoming_emails_to_a_Google_Sheets_spreadsheet_as_a_new_row..json) |
| Advanced AI Demo (Presented at AI Developers #14 meetup) | ai_process | n8n-nodes-langchain.chainretrievalqa, httprequest, n8n-nodes-langchain.lmchatanthropic | 🔴 High | [Advanced AI Demo (Presented at AI Developers #14 meetup).json](workflows/Advanced AI Demo (Presented at AI Developers #14 meetup).json) |
| Agentic Telegram AI bot with LangChain nodes and new tools | ai_process | n8n-nodes-langchain.memorybufferwindow, telegram, n8n-nodes-langchain.httprequest | 🟡 Medium | [Agentic Telegram AI bot with with LangChain nodes and new tools.json](workflows/Agentic Telegram AI bot with with LangChain nodes and new tools.json) |
| Agentic Telegram AI bot with LangChain nodes and new tools | ai_process | n8n-nodes-langchain.memorybufferwindow, telegram, n8n-nodes-langchain.httprequest | 🟡 Medium | [U8EOTtZvmZPMYc6m_Agentic_Telegram_AI_bot_with_LangChain_nodes_and_new_tools.json](workflows/U8EOTtZvmZPMYc6m_Agentic_Telegram_AI_bot_with_LangChain_nodes_and_new_tools.json) |
| AirQuality Scheduler | ai_process | n8n-nodes-langchain.think, httprequest, schedule | 🟡 Medium | [PcVz6j5XLU7Z9MPN_AirQuality_Scheduler.json](workflows/PcVz6j5XLU7Z9MPN_AirQuality_Scheduler.json) |
| Airtable markdown to html | ai_process | markdown, webhook, airtable | 🟡 Medium | [LMMle9xFHQxXUWQy_Airtable_markdown_to_html.json](workflows/LMMle9xFHQxXUWQy_Airtable_markdown_to_html.json) |
| Airtop Web Agent | ai_process | slack, n8n-nodes-langchain.outputparserstructured, airtop | 🔴 High | [TS1wT16JCcy1Dt9Q_Airtop_Web_Agent.json](workflows/TS1wT16JCcy1Dt9Q_Airtop_Web_Agent.json) |
| All-in-One Telegram/Baserow AI Assistant 🤖🧠 Voice/Photo/Save Notes/Long Term Mem | ai_process | baserow, n8n-nodes-langchain.memorybufferwindow, n8n-nodes-langchain.memorypostgreschat | 🔴 High | [Dctc6QKyRXK17oEq_All-in-One_Telegram_Baserow_AI_Assistant_🤖🧠_Voice_Photo_Save_Notes_Long_Term_Mem.json](workflows/Dctc6QKyRXK17oEq_All-in-One_Telegram_Baserow_AI_Assistant_🤖🧠_Voice_Photo_Save_Notes_Long_Term_Mem.json) |
| Amazon Ads AI Optimization | ai_process | n8n-nodes-langchain.chainllm, gmail, n8n-nodes-langchain.lmchatopenai | 🔴 High | [Agn9dzf5YTqcmQGN_Amazon_Ads_AI_Optimization.json](workflows/Agn9dzf5YTqcmQGN_Amazon_Ads_AI_Optimization.json) |
| Angie, Personal AI Assistant with Telegram Voice and Text | ai_process | n8n-nodes-langchain.memorybufferwindow, baserow, googlecalendar | 🔴 High | [Angie, Personal AI Assistant with Telegram Voice and Text.json](workflows/Angie, Personal AI Assistant with Telegram Voice and Text.json) |
| Ask questions about a PDF using AI | ai_process | n8n-nodes-langchain.chainretrievalqa, n8n-nodes-langchain.chat, n8n-nodes-langchain.embeddingsopenai | 🔴 High | [Ask questions about a PDF using AI.json](workflows/Ask questions about a PDF using AI.json) |
| Attachments Gmail to drive and google sheets | ai_process | n8n-nodes-langchain.chainllm, n8n-nodes-langchain.outputparserstructured, gmail | 🔴 High | [XnGZZfT5u0Cw1X3p_Attachments_Gmail_to_drive_and_google_sheets.json](workflows/XnGZZfT5u0Cw1X3p_Attachments_Gmail_to_drive_and_google_sheets.json) |
| Auto Categorise Outlook Emails with AI | ai_process | splitinbatches, microsoftoutlook, markdown | 🔴 High | [Auto Categorise Outlook Emails with AI.json](workflows/Auto Categorise Outlook Emails with AI.json) |
| Auto-Tag Blog Posts in WordPress with AI | ai_process | splitinbatches, n8n-nodes-langchain.outputparserautofixing, wordpress | 🔴 High | [Auto-Tag Blog Posts in WordPress with AI.json](workflows/Auto-Tag Blog Posts in WordPress with AI.json) |
| Auto-Tag Blog Posts in WordPress with AI | ai_process | splitinbatches, n8n-nodes-langchain.outputparserautofixing, wordpress | 🔴 High | [siXUnQhJpCJ9rHzu_Auto-Tag_Blog_Posts_in_WordPress_with_AI.json](workflows/siXUnQhJpCJ9rHzu_Auto-Tag_Blog_Posts_in_WordPress_with_AI.json) |
| Auto-create and publish AI social videos with Telegram, GPT-4 and Blotato | ai_process | httprequest, telegram, telegram | 🔴 High | [hiCTcf6srJl3Xsxh_Auto-create_and_publish_AI_social_videos_with_Telegram,_GPT-4_and_Blotato.json](workflows/hiCTcf6srJl3Xsxh_Auto-create_and_publish_AI_social_videos_with_Telegram,_GPT-4_and_Blotato.json) |
| Auto-label incoming Gmail messages with AI nodes | ai_process | n8n-nodes-langchain.chainllm, n8n-nodes-langchain.outputparserstructured, gmail | 🔴 High | [Auto-label incoming Gmail messages with AI nodes.json](workflows/Auto-label incoming Gmail messages with AI nodes.json) |
| Automate Blog Creation in Brand Voice with AI | ai_process | wordpress, n8n-nodes-langchain.chainllm, httprequest | 🔴 High | [Automate Blog Creation in Brand Voice with AI.json](workflows/Automate Blog Creation in Brand Voice with AI.json) |
| Automate Competitor Research with Exa.ai, Notion and AI Agents | ai_process | N/A | 🟢 Low | [Automate Competitor Research with Exa.ai, Notion and AI Agents.json](workflows/Automate Competitor Research with Exa.ai, Notion and AI Agents.json) |
| Automate Customer Support Issue Resolution using AI Text Classifier | ai_process | slack, n8n-nodes-langchain.chainllm, n8n-nodes-langchain.outputparserstructured | 🔴 High | [Automate Customer Support Issue Resolution using AI Text Classifier.json](workflows/Automate Customer Support Issue Resolution using AI Text Classifier.json) |
| Automate Image Validation Tasks using AI Vision | ai_process | n8n-nodes-langchain.chainllm, n8n-nodes-langchain.outputparserstructured, manual | 🟡 Medium | [Automate Image Validation Tasks using AI Vision.json](workflows/Automate Image Validation Tasks using AI Vision.json) |
| Automate LinkedIn Posts with AI | ai_process | linkedin, httprequest, notion | 🟡 Medium | [mb2MU4xOaT3NrvqN_Automate_LinkedIn_Posts_with_AI.json](workflows/mb2MU4xOaT3NrvqN_Automate_LinkedIn_Posts_with_AI.json) |
| Automate LinkedIn Posts with AI | ai_process | linkedin, httprequest, notion | 🟡 Medium | [Automate LinkedIn Outreach with Notion and OpenAI.json](workflows/Automate LinkedIn Outreach with Notion and OpenAI.json) |
| Automate Pinterest Analysis & AI-Powered Content Suggestions With Pinterest API | ai_process | airtable, gmail, httprequest | 🔴 High | [gP9EsxKN5agUGzDS_Automate_Pinterest_Analysis_&_AI-Powered_Content_Suggestions_With_Pinterest_API.json](workflows/gP9EsxKN5agUGzDS_Automate_Pinterest_Analysis_&_AI-Powered_Content_Suggestions_With_Pinterest_API.json) |
| Automate Pinterest Analysis & AI-Powered Content Suggestions With Pinterest API | ai_process | airtable, gmail, httprequest | 🔴 High | [Automate Pinterest Analysis & AI-Powered Content Suggestions With Pinterest API.json](workflows/Automate Pinterest Analysis & AI-Powered Content Suggestions With Pinterest API.json) |
| Automate Sales Meeting Prep with AI & APIFY Sent To WhatsApp | ai_process | n8n-nodes-langchain.chainllm, gmail, httprequest | 🔴 High | [Automate Sales Meeting Prep with AI & APIFY Sent To WhatsApp.json](workflows/Automate Sales Meeting Prep with AI & APIFY Sent To WhatsApp.json) |
| Automate Your RFP Process with OpenAI Assistants | ai_process | splitinbatches, slack, n8n-nodes-langchain.chainllm | 🔴 High | [Automate Your RFP Process with OpenAI Assistants.json](workflows/Automate Your RFP Process with OpenAI Assistants.json) |
| Automated AI image analysis and response via Telegram | ai_process | telegram, telegram, n8n-nodes-langchain.openai | 🟡 Medium | [Automated AI image analysis and response via Telegram.json](workflows/Automated AI image analysis and response via Telegram.json) |
| Automated Daily Weather Data Fetcher and Storage | ai_process | schedule, httprequest, airtable | 🟢 Low | [PHp3gKoyYfSztbTB_Automated_Daily_Weather_Data_Fetcher_and_Storage.json](workflows/PHp3gKoyYfSztbTB_Automated_Daily_Weather_Data_Fetcher_and_Storage.json) |
| Automated Form Submission Data Storage in Airtable | ai_process | airtable, form | 🟢 Low | [QObDE85a2ArfJkxV_Automated_Form_Submission_Data_Storage_in_Airtable.json](workflows/QObDE85a2ArfJkxV_Automated_Form_Submission_Data_Storage_in_Airtable.json) |
| Automated Research Report Generation with OpenAI, Wikipedia, Google Search, and Gmail/Telegram | ai_process | n8n-nodes-langchain.memorybufferwindow, n8n-nodes-langchain.outputparserstructured, gmail | 🔴 High | [EOJfPcM9PPWI1Rmp_Automated_Research_Report_Generation_with_OpenAI,_Wikipedia,_Google_Search,_and_Gmail_Telegram.json](workflows/EOJfPcM9PPWI1Rmp_Automated_Research_Report_Generation_with_OpenAI,_Wikipedia,_Google_Search,_and_Gmail_Telegram.json) |
| Automated Resume Review System Using OpenAI + Google Sheets | ai_process | n8n-nodes-langchain.chainllm, n8n-nodes-langchain.outputparserstructured, n8n-nodes-langchain.chainsummarization | 🔴 High | [IO0OrQ6ao4vm9urI_Automated_Resume_Review_System_Using_OpenAI_+_Google_Sheets.json](workflows/IO0OrQ6ao4vm9urI_Automated_Resume_Review_System_Using_OpenAI_+_Google_Sheets.json) |
| Automatically Send Daily Meeting List to Telegram | ai_process | schedule, googlecalendar, telegram | 🟡 Medium | [nV1xFcF5HWJcD6w7_Automatically_Send_Daily_Meeting_List_to_Telegram.json](workflows/nV1xFcF5HWJcD6w7_Automatically_Send_Daily_Meeting_List_to_Telegram.json) |
| Automating Betting Data Retrieval with TheOddsAPI and Airtable | ai_process | httprequest, schedule, airtable | 🟡 Medium | [6sBxOuYYcJjIBmVJ_Automating_Betting_Data_Retrieval_with_TheOddsAPI_and_Airtable.json](workflows/6sBxOuYYcJjIBmVJ_Automating_Betting_Data_Retrieval_with_TheOddsAPI_and_Airtable.json) |
| Autonomous AI crawler | ai_process | supabase, removeduplicates, n8n-nodes-langchain.outputparserstructured | 🔴 High | [Autonomous AI crawler.json](workflows/Autonomous AI crawler.json) |
| BambooHR AI-Powered Company Policies and Benefits Chatbot | ai_process | n8n-nodes-langchain.outputparserautofixing, n8n-nodes-langchain.outputparserstructured, n8n-nodes-langchain.informationextractor | 🔴 High | [dYjQS1bJmVSAxNnj_BambooHR_AI-Powered_Company_Policies_and_Benefits_Chatbot.json](workflows/dYjQS1bJmVSAxNnj_BambooHR_AI-Powered_Company_Policies_and_Benefits_Chatbot.json) |
| BambooHR AI-Powered Company Policies and Benefits Chatbot | ai_process | n8n-nodes-langchain.outputparserautofixing, n8n-nodes-langchain.outputparserstructured, n8n-nodes-langchain.informationextractor | 🔴 High | [BambooHR AI-Powered Company Policies and Benefits Chatbot.json](workflows/BambooHR AI-Powered Company Policies and Benefits Chatbot.json) |
| Basic Automatic Gmail Email Labelling with OpenAI and Gmail API | ai_process | n8n-nodes-langchain.memorybufferwindow, gmail, n8n-nodes-langchain.lmchatopenai | 🟡 Medium | [Basic Automatic Gmail Email Labelling with OpenAI and Gmail API.json](workflows/Basic Automatic Gmail Email Labelling with OpenAI and Gmail API.json) |
| Blockchain DEX Screener Insights Agent | ai_process | n8n-nodes-langchain.memorybufferwindow, n8n-nodes-langchain.chat, n8n-nodes-langchain.httprequest | 🔴 High | [1ZfA8Do3j7lCB3zF_Blockchain_DEX_Screener_Insights_Agent.json](workflows/1ZfA8Do3j7lCB3zF_Blockchain_DEX_Screener_Insights_Agent.json) |
| Breakdown Documents into Study Notes using Templating MistralAI and Qdrant | ai_process | n8n-nodes-langchain.chainretrievalqa, extractfromfile, converttofile | 🔴 High | [Breakdown Documents into Study Notes using Templating MistralAI and Qdrant.json](workflows/Breakdown Documents into Study Notes using Templating MistralAI and Qdrant.json) |
| Build Custom AI Agent with LangChain & Gemini (Self-Hosted) | ai_process | n8n-nodes-langchain.memorybufferwindow, n8n-nodes-langchain.chat, n8n-nodes-langchain.code | 🟡 Medium | [yCIEiv9QUHP8pNfR_Build_Custom_AI_Agent_with_LangChain_&_Gemini_(Self-Hosted).json](workflows/yCIEiv9QUHP8pNfR_Build_Custom_AI_Agent_with_LangChain_&_Gemini_(Self-Hosted).json) |
| Build Your Own Image Search Using AI Object Detection, CDN and ElasticSearchBuild Your Own Image Search Using AI Object Detection, CDN and ElasticSearch | ai_process | elasticsearch, httprequest, manual | 🔴 High | [Build Your Own Image Search Using AI Object Detection, CDN and ElasticSearchBuild Your Own Image Search Using AI Object Detection, CDN and ElasticSearch.json](workflows/Build Your Own Image Search Using AI Object Detection, CDN and ElasticSearchBuild Your Own Image Search Using AI Object Detection, CDN and ElasticSearch.json) |
| Build a Financial Documents Assistant using Qdrant and Mistral.ai | ai_process | n8n-nodes-langchain.chainretrievalqa, n8n-nodes-langchain.chat, n8n-nodes-langchain.lmchatmistralcloud | 🔴 High | [Build a Financial Documents Assistant using Qdrant and Mistral.ai.json](workflows/Build a Financial Documents Assistant using Qdrant and Mistral.ai.json) |
| Build a Phone Agent to qualify outbound leads and inbound calls with RetellAI -vide | ai_process | gmail, httprequest, webhook | 🔴 High | [QO4Mg23JvVfNCICy_Build_a_Phone_Agent_to_qualify_outbound_leads_and_inbound_calls_with_RetellAI_-vide.json](workflows/QO4Mg23JvVfNCICy_Build_a_Phone_Agent_to_qualify_outbound_leads_and_inbound_calls_with_RetellAI_-vide.json) |
| Build a Tax Code Assistant with Qdrant, Mistral.ai and OpenAI | ai_process | httprequest, extractfromfile, n8n-nodes-langchain.embeddingsmistralcloud | 🔴 High | [Build a Tax Code Assistant with Qdrant, Mistral.ai and OpenAI.json](workflows/Build a Tax Code Assistant with Qdrant, Mistral.ai and OpenAI.json) |
| Build an MCP server with Airtable | ai_process | n8n-nodes-langchain.memorybufferwindow, airtable, n8n-nodes-langchain.chat | 🔴 High | [kS9EfgZeaK3QV6Mw_Build_an_MCP_server_with_Airtable.json](workflows/kS9EfgZeaK3QV6Mw_Build_an_MCP_server_with_Airtable.json) |
| Build an OpenAI Assistant with Google Drive Integration | ai_process | n8n-nodes-langchain.memorybufferwindow, n8n-nodes-langchain.chat, manual | 🟡 Medium | [AjJ7O98qjw8XVirk_Build_an_OpenAI_Assistant_with_Google_Drive_Integration.json](workflows/AjJ7O98qjw8XVirk_Build_an_OpenAI_Assistant_with_Google_Drive_Integration.json) |
| Build an OpenAI Assistant with Google Drive Integration | ai_process | n8n-nodes-langchain.memorybufferwindow, n8n-nodes-langchain.chat, manual | 🟡 Medium | [Build an OpenAI Assistant with Google Drive Integration.json](workflows/Build an OpenAI Assistant with Google Drive Integration.json) |
| Build your first AI MCP Server | ai_process | n8n-nodes-langchain.memorybufferwindow, n8n-nodes-langchain.chat, httprequest | 🔴 High | [8n0VYmvJgISwezyz_Build_your_first_AI_MCP_Server.json](workflows/8n0VYmvJgISwezyz_Build_your_first_AI_MCP_Server.json) |
| Building RAG Chatbot for Movie Recommendations with Qdrant and Open AI | ai_process | httprequest, extractfromfile, n8n-nodes-langchain.chat | 🔴 High | [a58HZKwcOy7lmz56_Building_RAG_Chatbot_for_Movie_Recommendations_with_Qdrant_and_Open_AI.json](workflows/a58HZKwcOy7lmz56_Building_RAG_Chatbot_for_Movie_Recommendations_with_Qdrant_and_Open_AI.json) |
| Building RAG Chatbot for Movie Recommendations with Qdrant and Open AI | ai_process | httprequest, extractfromfile, n8n-nodes-langchain.chat | 🔴 High | [Building RAG Chatbot for Movie Recommendations with Qdrant and Open AI.json](workflows/Building RAG Chatbot for Movie Recommendations with Qdrant and Open AI.json) |
| Business WhatsApp AI RAG Chatbot | ai_process | n8n-nodes-langchain.memorybufferwindow, n8n-nodes-langchain.vectorstore, whatsapp | 🔴 High | [NLOITjwt4iZK16Qq_Business_WhatsApp_AI_RAG_Chatbot.json](workflows/NLOITjwt4iZK16Qq_Business_WhatsApp_AI_RAG_Chatbot.json) |
| Business WhatsApp AI RAG Chatbot | ai_process | n8n-nodes-langchain.memorybufferwindow, whatsapp, n8n-nodes-langchain.textsplittertokensplitter | 🔴 High | [Complete business WhatsApp AI-Powered RAG Chatbot using OpenAI.json](workflows/Complete business WhatsApp AI-Powered RAG Chatbot using OpenAI.json) |
| CV Resume PDF Parsing with Multimodal Vision AI | ai_process | n8n-nodes-langchain.chainllm, n8n-nodes-langchain.outputparserstructured, httprequest | 🔴 High | [CV Resume PDF Parsing with Multimodal Vision AI.json](workflows/CV Resume PDF Parsing with Multimodal Vision AI.json) |
| CV Screening with OpenAI | ai_process | httprequest, manual, extractfromfile | 🟡 Medium | [CV Screening with OpenAI.json](workflows/CV Screening with OpenAI.json) |
| Chat with GitHub OpenAPI Specification using RAG (Pinecone and OpenAI) | ai_process | n8n-nodes-langchain.memorybufferwindow, n8n-nodes-langchain.vectorstore, n8n-nodes-langchain.chat | 🔴 High | [Chat with GitHub API Documentation_ RAG-Powered Chatbot with Pinecone & OpenAI.json](workflows/Chat with GitHub API Documentation_ RAG-Powered Chatbot with Pinecone & OpenAI.json) |
| Chat with OpenAI Assistant (by adding a memory) | ai_process | n8n-nodes-langchain.memorybufferwindow, n8n-nodes-langchain.calculator, n8n-nodes-langchain.openaiassistant | 🔴 High | [Chat with OpenAI Assistant (by adding a memory).json](workflows/Chat with OpenAI Assistant (by adding a memory).json) |
| Chat with OpenAIs GPT via a simple Telegram Bot | ai_process | n8n-nodes-langchain.lmchatopenai, telegram, telegram | 🟢 Low | [Chat with OpenAIs GPT via a simple Telegram Bot.json](workflows/Chat with OpenAIs GPT via a simple Telegram Bot.json) |
| Chat with PDF docs using AI (quoting sources) | ai_process | n8n-nodes-langchain.chainllm, n8n-nodes-langchain.outputparserstructured, n8n-nodes-langchain.chat | 🔴 High | [Chat with PDF docs using AI (quoting sources).json](workflows/Chat with PDF docs using AI (quoting sources).json) |
| Chatbot AI | ai_process | n8n-nodes-langchain.lmchatazureopenai, httprequest, webhook | 🔴 High | [ghfbOYrOSiQVAbl5_Chatbot_AI.json](workflows/ghfbOYrOSiQVAbl5_Chatbot_AI.json) |
| Check for valid Hubspot contact email | ai_process | hubspot, onesimpleapi, slack | 🟢 Low | [88_Check_for_valid_Hubspot_contact_email.json](workflows/88_Check_for_valid_Hubspot_contact_email.json) |
| Check for valid Mautic contact email | ai_process | onesimpleapi, itemlists, mautic | 🟡 Medium | [86_Check_for_valid_Mautic_contact_email.json](workflows/86_Check_for_valid_Mautic_contact_email.json) |
| Cocktail Recipe Sharing | ai_process | rocketchat, httprequest, bannerbear | 🟢 Low | [46_Cocktail_Recipe_Sharing.json](workflows/46_Cocktail_Recipe_Sharing.json) |
| CoinMarketCap_AI_Data_Analyst_Agent | ai_process | n8n-nodes-langchain.memorybufferwindow, n8n-nodes-langchain.lmchatopenai, n8n-nodes-langchain.workflow | 🟡 Medium | [mE7Zvhv1lOd4Q3xY_CoinMarketCap_AI_Data_Analyst_Agent.json](workflows/mE7Zvhv1lOd4Q3xY_CoinMarketCap_AI_Data_Analyst_Agent.json) |
| Compose reply draft in Gmail with OpenAI Assistant | ai_process | splitinbatches, gmail, httprequest | 🔴 High | [Compose reply draft in Gmail with OpenAI Assistant.json](workflows/Compose reply draft in Gmail with OpenAI Assistant.json) |
| Connect Airtable Contacts to telli for Automated AI Voice Call Scheduling | ai_process | httprequest, airtable | 🟢 Low | [f3BtfIEQ7lWiXBWQ_Connect_Airtable_Contacts_to_telli_for_Automated_AI_Voice_Call_Scheduling.json](workflows/f3BtfIEQ7lWiXBWQ_Connect_Airtable_Contacts_to_telli_for_Automated_AI_Voice_Call_Scheduling.json) |
| Conversational Interviews with AI Agents and n8n Forms | ai_process | n8n-nodes-langchain.memorybufferwindow, respondtowebhook, crypto | 🔴 High | [Conversational Interviews with AI Agents and n8n Forms.json](workflows/Conversational Interviews with AI Agents and n8n Forms.json) |
| Convert the JSON data received from the CocktailDB API in XML | ai_process | xml, httprequest, manual | 🟢 Low | [55_Convert_the_JSON_data_received_from_the_CocktailDB_API_in_XML.json](workflows/55_Convert_the_JSON_data_received_from_the_CocktailDB_API_in_XML.json) |
| Create AI-Ready Vector Datasets for LLMs with Bright Data, Gemini & Pinecone | ai_process | n8n-nodes-langchain.chainllm, n8n-nodes-langchain.outputparserstructured, httprequest | 🔴 High | [3Lih0LVosR8dZbla_Create_AI-Ready_Vector_Datasets_for_LLMs_with_Bright_Data,_Gemini_&_Pinecone.json](workflows/3Lih0LVosR8dZbla_Create_AI-Ready_Vector_Datasets_for_LLMs_with_Bright_Data,_Gemini_&_Pinecone.json) |
| Create Email Campaign From LinkedIn Post Interactions | ai_process | hubspot, lemlist, airtable | 🔴 High | [121_Create_Email_Campaign_From_LinkedIn_Post_Interactions.json](workflows/121_Create_Email_Campaign_From_LinkedIn_Post_Interactions.json) |
| Create Nextcloud Deck card from email | ai_process | httprequest, emailreadimap | 🟢 Low | [1_Create_Nextcloud_Deck_card_from_email.json](workflows/1_Create_Nextcloud_Deck_card_from_email.json) |
| Create a Branded AI-Powered Website Chatbot | ai_process | n8n-nodes-langchain.memorybufferwindow, n8n-nodes-langchain.chat, httprequest | 🔴 High | [Create a Branded AI-Powered Website Chatbot.json](workflows/Create a Branded AI-Powered Website Chatbot.json) |
| Create entry in Mailchimp from Airtable | ai_process | mailchimp, airtable, cron | 🟢 Low | [1_Create_entry_in_Mailchimp_from_Airtable.json](workflows/1_Create_entry_in_Mailchimp_from_Airtable.json) |
| Create, update and get a subscriber using the MailerLite node | ai_process | mailerlite, manual | 🟢 Low | [96_Create,_update_and_get_a_subscriber_using_the_MailerLite_node.json](workflows/96_Create,_update_and_get_a_subscriber_using_the_MailerLite_node.json) |
| Create, update, and get a profile in Humantic AI | ai_process | humanticai, httprequest, manual | 🟢 Low | [127_Create,_update,_and_get_a_profile_in_Humantic_AI.json](workflows/127_Create,_update,_and_get_a_profile_in_Humantic_AI.json) |
| Create, update, and get a profile in Humantic AI | ai_process | humanticai, httprequest, manual | 🟢 Low | [Create, update, and get a profile in Humantic AI.json](workflows/Create, update, and get a profile in Humantic AI.json) |
| Create, update, and get an issue on Taiga | ai_process | taiga, manual | 🟢 Low | [69_Create,_update,_and_get_an_issue_on_Taiga.json](workflows/69_Create,_update,_and_get_an_issue_on_Taiga.json) |
| Creating a AI Slack Bot with Google Gemini | ai_process | n8n-nodes-langchain.memorybufferwindow, slack, webhook | 🟡 Medium | [Creating a AI Slack Bot with Google Gemini.json](workflows/Creating a AI Slack Bot with Google Gemini.json) |
| Daily AI News Translation & Summary with GPT-4 and Telegram Delivery | ai_process | httprequest, schedule, n8n-nodes-langchain.lmchatopenai | 🟡 Medium | [4AG83ybt0S3WQbkS_Daily_AI_News_Translation_&_Summary_with_GPT-4_and_Telegram_Delivery.json](workflows/4AG83ybt0S3WQbkS_Daily_AI_News_Translation_&_Summary_with_GPT-4_and_Telegram_Delivery.json) |
| Daily Journal Reminder | ai_process | functionitem, telegram, cron | 🟢 Low | [1_Daily_Journal_Reminder.json](workflows/1_Daily_Journal_Reminder.json) |
| Daily Language Learning | ai_process | cron, airtable, lingvanex | 🟡 Medium | [7_Daily_Language_Learning.json](workflows/7_Daily_Language_Learning.json) |
| Daily Podcast Summary | ai_process | gmail, httprequest, schedule | 🔴 High | [Daily Podcast Summary.json](workflows/Daily Podcast Summary.json) |
| Daily Text Affirmations | ai_process | httprequest, telegram, cron | 🟢 Low | [2_Daily_Text_Affirmations.json](workflows/2_Daily_Text_Affirmations.json) |
| Daily meetings summarization with Gemini AI | ai_process | slack, googlecalendar, schedule | 🟡 Medium | [Daily meetings summarization with Gemini AI.json](workflows/Daily meetings summarization with Gemini AI.json) |
| Daily meetings summarization with Gemini AI | ai_process | slack, googlecalendar, schedule | 🟡 Medium | [jAML9xW28lOdsObH_Daily_meetings_summarization_with_Gemini_AI.json](workflows/jAML9xW28lOdsObH_Daily_meetings_summarization_with_Gemini_AI.json) |
| Daily poems in Telegram | ai_process | lingvanex, httprequest, telegram | 🟢 Low | [3_Daily_poems_in_Telegram.json](workflows/3_Daily_poems_in_Telegram.json) |
| Deduplicate Scraping AI Grants for Eligibility using AI | ai_process | gmail, httprequest, html | 🔴 High | [Deduplicate Scraping AI Grants for Eligibility using AI.json](workflows/Deduplicate Scraping AI Grants for Eligibility using AI.json) |
| Discord AI bot | ai_process | webhook, openai, manual | 🟡 Medium | [Discord AI-powered bot.json](workflows/Discord AI-powered bot.json) |
| Discord AI bot | ai_process | webhook, openai, manual | 🟡 Medium | [180_Discord_AI_bot.json](workflows/180_Discord_AI_bot.json) |
| Dynamic Form with AI | ai_process | n8n-nodes-langchain.chainllm, n8n-nodes-langchain.outputparserstructured, form | 🔴 High | [ZkIH2ygj2BNSfMOh_Dynamic_Form_with_AI.json](workflows/ZkIH2ygj2BNSfMOh_Dynamic_Form_with_AI.json) |
| Dynamically create tables in Airtable for your Webflow form submissions | ai_process | httprequest, webflow, airtable | 🔴 High | [IvIzphIxPj1rZ3az_Dynamically_create_tables_in_Airtable_for_your_Webflow_form_submissions.json](workflows/IvIzphIxPj1rZ3az_Dynamically_create_tables_in_Airtable_for_your_Webflow_form_submissions.json) |
| ERP AI chatbot for Odoo sales module | ai_process | n8n-nodes-langchain.memorybufferwindow, n8n-nodes-langchain.calculator, n8n-nodes-langchain.chat | 🔴 High | [n8cwEZfJLGn15Lqx_ERP_AI_chatbot_for_Odoo_sales_module.json](workflows/n8cwEZfJLGn15Lqx_ERP_AI_chatbot_for_Odoo_sales_module.json) |
| Easily Compare LLMs Using OpenAI and Google Sheets | ai_process | splitinbatches, n8n-nodes-langchain.memorybufferwindow, n8n-nodes-langchain.chat | 🔴 High | [_Easily_Compare_LLMs_Using_OpenAI_and_Google_Sheets.json](workflows/_Easily_Compare_LLMs_Using_OpenAI_and_Google_Sheets.json) |
| Effortless Email Management with AI | ai_process | n8n-nodes-langchain.lmchatdeepseek, n8n-nodes-langchain.textsplittertokensplitter, gmail | 🔴 High | [nkPjDxMrrkKbgHaV_Effortless_Email_Management_with_AI.json](workflows/nkPjDxMrrkKbgHaV_Effortless_Email_Management_with_AI.json) |
| Effortless Email Management with AI | ai_process | n8n-nodes-langchain.lmchatdeepseek, n8n-nodes-langchain.textsplittertokensplitter, gmail | 🔴 High | [Effortless Email Management with AI-Powered Summarization & Review.json](workflows/Effortless Email Management with AI-Powered Summarization & Review.json) |
| Email | ai_process | emailreadimap, cortex, thehive | 🟡 Medium | [4_Email.json](workflows/4_Email.json) |
| Email AI Auto-responder. Summerize and send email | ai_process | n8n-nodes-langchain.chainllm, n8n-nodes-langchain.textsplittertokensplitter, emailsend | 🔴 High | [q8IFGLeOCGSfoWZu_Email_AI_Auto-responder._Summerize_and_send_email.json](workflows/q8IFGLeOCGSfoWZu_Email_AI_Auto-responder._Summerize_and_send_email.json) |
| Email AI Auto-responder. Summerize and send email | ai_process | n8n-nodes-langchain.chainllm, n8n-nodes-langchain.textsplittertokensplitter, emailsend | 🔴 High | [AI-Powered Email Automation for Business_ Summarize & Respond with RAG.json](workflows/AI-Powered Email Automation for Business_ Summarize & Respond with RAG.json) |
| Email Subscription Service with n8n Forms, Airtable and AI | ai_process | n8n-nodes-langchain.memorybufferwindow, executiondata, n8n-nodes-langchain.lmchatgroq | 🔴 High | [Email Subscription Service with n8n Forms, Airtable and AI.json](workflows/Email Subscription Service with n8n Forms, Airtable and AI.json) |
| Email Subscription Service with n8n Forms, Airtable and AI (1) | ai_process | n8n-nodes-langchain.memorybufferwindow, executiondata, n8n-nodes-langchain.lmchatgroq | 🔴 High | [Email Subscription Service with n8n Forms, Airtable and AI (1).json](workflows/Email Subscription Service with n8n Forms, Airtable and AI (1).json) |
| Email Summary Agent | ai_process | gmail, schedule, n8n-nodes-langchain.openai | 🟡 Medium | [Email Summary Agent.json](workflows/Email Summary Agent.json) |
| Email Summary Agent | ai_process | gmail, schedule, n8n-nodes-langchain.openai | 🟡 Medium | [M8oLW9Qd59zNJzg2_Email_Summary_Agent.json](workflows/M8oLW9Qd59zNJzg2_Email_Summary_Agent.json) |
| Email body parser by aprenden8n.com | ai_process | functionitem, manual | 🟢 Low | [340_Email_body_parser_by_aprenden8n.com.json](workflows/340_Email_body_parser_by_aprenden8n.com.json) |
| Email form | ai_process | sendgrid, hunter, form | 🟡 Medium | [1blBTEfOEjamDB0N_Email_form.json](workflows/1blBTEfOEjamDB0N_Email_form.json) |
| Email mailbox as Todoist tasks | ai_process | n8n-nodes-langchain.outputparserstructured, gmail, schedule | 🔴 High | [WUX0BsRA1dbzTKnl_Email_mailbox_as_Todoist_tasks.json](workflows/WUX0BsRA1dbzTKnl_Email_mailbox_as_Todoist_tasks.json) |
| Email verification with Icypeas (single) | ai_process | httprequest, manual | 🟢 Low | [IwOOVikQC7cn9VTv_Email_verification_with_Icypeas_(single).json](workflows/IwOOVikQC7cn9VTv_Email_verification_with_Icypeas_(single).json) |
| Enhance Chat Responses with Real-Time Search Data via Bright Data & Gemini AI | ai_process | n8n-nodes-langchain.memorybufferwindow, n8n-nodes-langchain.chat, n8n-nodes-langchain.httprequest | 🔴 High | [8jdT4wXjV5NljqKa_Enhance_Chat_Responses_with_Real-Time_Search_Data_via_Bright_Data_&_Gemini_AI.json](workflows/8jdT4wXjV5NljqKa_Enhance_Chat_Responses_with_Real-Time_Search_Data_via_Bright_Data_&_Gemini_AI.json) |
| Enrich Company Data from Google Sheet with OpenAI Agent and Scraper Tool | ai_process | splitinbatches, n8n-nodes-langchain.outputparserstructured, httprequest | 🔴 High | [TfwQRZkTBtykx1rM_Enrich_Company_Data_from_Google_Sheet_with_OpenAI_Agent_and_Scraper_Tool.json](workflows/TfwQRZkTBtykx1rM_Enrich_Company_Data_from_Google_Sheet_with_OpenAI_Agent_and_Scraper_Tool.json) |
| Enrich FAQ sections on your website pages at scale with AI | ai_process | splitinbatches, strapi, wordpress | 🔴 High | [Enrich FAQ sections on your website pages at scale with AI.json](workflows/Enrich FAQ sections on your website pages at scale with AI.json) |
| Enrich Property Inventory Survey with Image Recognition and AI Agent | ai_process | n8n-nodes-langchain.outputparserstructured, httprequest, n8n-nodes-langchain.lmchatopenai | 🔴 High | [Enrich Property Inventory Survey with Image Recognition and AI Agent.json](workflows/Enrich Property Inventory Survey with Image Recognition and AI Agent.json) |
| Extract & Summarize Bing Copilot Search Results with Gemini AI and Bright Data | ai_process | n8n-nodes-langchain.chainllm, n8n-nodes-langchain.outputparserstructured, httprequest | 🔴 High | [AnbedV2Ntx97sfed_Extract_&_Summarize_Bing_Copilot_Search_Results_with_Gemini_AI_and_Bright_Data.json](workflows/AnbedV2Ntx97sfed_Extract_&_Summarize_Bing_Copilot_Search_Results_with_Gemini_AI_and_Bright_Data.json) |
| Extract & Summarize Wikipedia Data with Bright Data and Gemini AI | ai_process | n8n-nodes-langchain.chainllm, httprequest, n8n-nodes-langchain.chainsummarization | 🟡 Medium | [sczRNO4u1HYc5YV7_Extract_&_Summarize_Wikipedia_Data_with_Bright_Data_and_Gemini_AI.json](workflows/sczRNO4u1HYc5YV7_Extract_&_Summarize_Wikipedia_Data_with_Bright_Data_and_Gemini_AI.json) |
| Extract Business Leads from Google Maps with Dumpling AI to Google Sheets | ai_process | httprequest, manual, googlesheets | 🟢 Low | [YZpFvpXOTYkBpiUU_Extract_Business_Leads_from_Google_Maps_with_Dumpling_AI_to_Google_Sheets.json](workflows/YZpFvpXOTYkBpiUU_Extract_Business_Leads_from_Google_Maps_with_Dumpling_AI_to_Google_Sheets.json) |
| Extract expenses from emails and add to Google Sheet | ai_process | mindee, googlesheets, emailreadimap | 🟡 Medium | [90_Extract_expenses_from_emails_and_add_to_Google_Sheet.json](workflows/90_Extract_expenses_from_emails_and_add_to_Google_Sheet.json) |
| Extract insights & analyse YouTube comments via AI Agent chat | ai_process | n8n-nodes-langchain.memorypostgreschat, n8n-nodes-langchain.chat, httprequest | 🔴 High | [Extract insights & analyse YouTube comments via AI Agent chat.json](workflows/Extract insights & analyse YouTube comments via AI Agent chat.json) |
| Extract spend details (template) | ai_process | n8n-nodes-langchain.chainllm, n8n-nodes-langchain.outputparserstructured, gmail | 🔴 High | [Extract spending history from gmail to google sheet.json](workflows/Extract spending history from gmail to google sheet.json) |
| Extract spend details (template) | ai_process | n8n-nodes-langchain.chainllm, n8n-nodes-langchain.outputparserstructured, gmail | 🔴 High | [nkMjcOC4hpte1a0t_Extract_spend_details_(template).json](workflows/nkMjcOC4hpte1a0t_Extract_spend_details_(template).json) |
| Extract text from PDF and image using Vertex AI (Gemini) into CSV | ai_process | n8n-nodes-langchain.chainllm, httprequest, n8n-nodes-langchain.lmchatgooglegemini | 🔴 High | [Extract text from PDF and image using Vertex AI (Gemini) into CSV.json](workflows/Extract text from PDF and image using Vertex AI (Gemini) into CSV.json) |
| Extract text from PDF and image using Vertex AI (Gemini) into CSV | ai_process | n8n-nodes-langchain.chainllm, httprequest, n8n-nodes-langchain.lmchatgooglegemini | 🔴 High | [sUIPemKdKqmUQFt6_Extract_text_from_PDF_and_image_using_Vertex_AI_(Gemini)_into_CSV.json](workflows/sUIPemKdKqmUQFt6_Extract_text_from_PDF_and_image_using_Vertex_AI_(Gemini)_into_CSV.json) |
| Fine-tuning with OpenAI models | ai_process | n8n-nodes-langchain.chat, httprequest, n8n-nodes-langchain.lmchatopenai | 🟡 Medium | [gAzsjTGbfWuvAObi_Fine-tuning_with_OpenAI_models.json](workflows/gAzsjTGbfWuvAObi_Fine-tuning_with_OpenAI_models.json) |
| Fine-tuning with OpenAI models | ai_process | n8n-nodes-langchain.chat, httprequest, n8n-nodes-langchain.lmchatopenai | 🟡 Medium | [Automated End-to-End Fine-Tuning of OpenAI Models with Google Drive Integration.json](workflows/Automated End-to-End Fine-Tuning of OpenAI Models with Google Drive Integration.json) |
| Flux AI Image Generator | ai_process | respondtowebhook, httprequest, form | 🔴 High | [Flux AI Image Generator.json](workflows/Flux AI Image Generator.json) |
| Flux Dev Image Generation Fal.ai | ai_process | httprequest, manual, googledrive | 🟡 Medium | [nJwkSOrJIFvutw1n_Flux_Dev_Image_Generation_Fal.ai.json](workflows/nJwkSOrJIFvutw1n_Flux_Dev_Image_Generation_Fal.ai.json) |
| Flux Dev Image Generation Fal.ai | ai_process | httprequest, manual, googledrive | 🟡 Medium | [Flux Dev Image Generation (Fal.ai) to Google Drive.json](workflows/Flux Dev Image Generation (Fal.ai) to Google Drive.json) |
| Forward Filtered Gmail Notifications to Telegram Chat | ai_process | gmail, telegram | 🟢 Low | [AvXlqUiuc1qJSwxf_Forward_Filtered_Gmail_Notifications_to_Telegram_Chat.json](workflows/AvXlqUiuc1qJSwxf_Forward_Filtered_Gmail_Notifications_to_Telegram_Chat.json) |
| Forward Netflix emails to multiple email addresses with GMail and Mailjet | ai_process | mailjet, gmail | 🟡 Medium | [pkw1vY5q1p2nNfNC_Forward_Netflix_emails_to_multiple_email_addresses_with_GMail_and_Mailjet.json](workflows/pkw1vY5q1p2nNfNC_Forward_Netflix_emails_to_multiple_email_addresses_with_GMail_and_Mailjet.json) |
| Get Airtable data in Obsidian Notes | ai_process | airtable, webhook, n8n-nodes-langchain.lmchatopenai | 🟡 Medium | [Get Airtable data via AI and Obsidian Notes.json](workflows/Get Airtable data via AI and Obsidian Notes.json) |
| Get Airtable data in Obsidian Notes | ai_process | airtable, webhook, n8n-nodes-langchain.lmchatopenai | 🟡 Medium | [aZSJ2BZQhNduZZ8w_Get_Airtable_data_in_Obsidian_Notes.json](workflows/aZSJ2BZQhNduZZ8w_Get_Airtable_data_in_Obsidian_Notes.json) |
| Get analytics of a website and store it Airtable | ai_process | googleanalytics, manual, airtable | 🟢 Low | [205_Get_analytics_of_a_website_and_store_it_Airtable.json](workflows/205_Get_analytics_of_a_website_and_store_it_Airtable.json) |
| Get details of a forum in Disqus | ai_process | disqus, manual | 🟢 Low | [119_Get_details_of_a_forum_in_Disqus.json](workflows/119_Get_details_of_a_forum_in_Disqus.json) |
| Get messages with a certain label, remove the label, and add a new one | ai_process | gmail, manual | 🟢 Low | [175_Get_messages_with_a_certain_label,_remove_the_label,_and_add_a_new_one.json](workflows/175_Get_messages_with_a_certain_label,_remove_the_label,_and_add_a_new_one.json) |
| Get the logo, icon, and information of a company and store it in Airtable | ai_process | airtable, manual, brandfetch | 🟢 Low | [176_Get_the_logo,_icon,_and_information_of_a_company_and_store_it_in_Airtable.json](workflows/176_Get_the_logo,_icon,_and_information_of_a_company_and_store_it_in_Airtable.json) |
| Gmail AI auto-responder: create draft replies to incoming emails | ai_process | n8n-nodes-langchain.chainllm, n8n-nodes-langchain.outputparserstructured, gmail | 🟡 Medium | [Gmail AI Auto-Responder_ Create Draft Replies to incoming emails.json](workflows/Gmail AI Auto-Responder_ Create Draft Replies to incoming emails.json) |
| Gmail MCP Server | ai_process | gmail, n8n-nodes-langchain.mcp | 🔴 High | [QaMO9ji6T6vTZHQ4_Gmail_MCP_Server.json](workflows/QaMO9ji6T6vTZHQ4_Gmail_MCP_Server.json) |
| Gmail to Vector Embeddings with PGVector and Ollama | ai_process | splitinbatches, postgres, gmail | 🔴 High | [ZiIoKEClTk83g1Jt_Gmail_to_Vector_Embeddings_with_PGVector_and_Ollama.json](workflows/ZiIoKEClTk83g1Jt_Gmail_to_Vector_Embeddings_with_PGVector_and_Ollama.json) |
| Google Maps Email Scraper Template | ai_process | splitinbatches, httprequest, manual | 🔴 High | [2567_Google_Maps_Email_Scraper_Template.json](workflows/2567_Google_Maps_Email_Scraper_Template.json) |
| Google Sheet to Mailchimp | ai_process | googlesheets, mailchimp, interval | 🟢 Low | [1_Google_Sheet_to_Mailchimp.json](workflows/1_Google_Sheet_to_Mailchimp.json) |
| HR Job Posting and Evaluation with AI | ai_process | airtable, n8n-nodes-langchain.outputparserstructured, emailsend | 🔴 High | [HR Job Posting and Evaluation with AI.json](workflows/HR Job Posting and Evaluation with AI.json) |
| HR Job Posting and Evaluation with AI | ai_process | airtable, n8n-nodes-langchain.outputparserstructured, emailsend | 🔴 High | [eMxH0GjgfWEvBDic_HR_Job_Posting_and_Evaluation_with_AI.json](workflows/eMxH0GjgfWEvBDic_HR_Job_Posting_and_Evaluation_with_AI.json) |
| HR-focused automation pipeline with AI | ai_process | n8n-nodes-langchain.chainllm, n8n-nodes-langchain.outputparserstructured, n8n-nodes-langchain.chainsummarization | 🔴 High | [AI Automated HR Workflow for CV Analysis and Candidate Evaluation.json](workflows/AI Automated HR Workflow for CV Analysis and Candidate Evaluation.json) |
| HR-focused automation pipeline with AI | ai_process | n8n-nodes-langchain.chainllm, n8n-nodes-langchain.outputparserstructured, n8n-nodes-langchain.chainsummarization | 🔴 High | [t1P14FvfibKYCh3E_HR-focused_automation_pipeline_with_AI.json](workflows/t1P14FvfibKYCh3E_HR-focused_automation_pipeline_with_AI.json) |
| Handling Appointment Leads and Follow-up With Twilio, Cal.com and AI | ai_process | n8n-nodes-langchain.outputparserautofixing, n8n-nodes-langchain.chainllm, n8n-nodes-langchain.outputparserstructured | 🔴 High | [Handling Appointment Leads and Follow-up With Twilio, Cal.com and AI.json](workflows/Handling Appointment Leads and Follow-up With Twilio, Cal.com and AI.json) |
| Handling Job Application Submissions with AI and n8n Forms | ai_process | n8n-nodes-langchain.chainllm, n8n-nodes-langchain.outputparserstructured, n8n-nodes-langchain.textclassifier | 🔴 High | [Handling Job Application Submissions with AI and n8n Forms.json](workflows/Handling Job Application Submissions with AI and n8n Forms.json) |
| Host Your Own AI Deep Research Agent with n8n, Apify and OpenAI o3 | ai_process | N/A | 🟢 Low | [Host Your Own AI Deep Research Agent with n8n, Apify and OpenAI o3.json](workflows/Host Your Own AI Deep Research Agent with n8n, Apify and OpenAI o3.json) |
| IT Ops AI SlackBot Workflow - Chat with your knowledge base | ai_process | n8n-nodes-langchain.memorybufferwindow, slack, webhook | 🔴 High | [IT Ops AI SlackBot Workflow - Chat with your knowledge base.json](workflows/IT Ops AI SlackBot Workflow - Chat with your knowledge base.json) |
| Image Creation with OpenAI and Telegram | ai_process | telegram, telegram, n8n-nodes-langchain.openai | 🟡 Medium | [Image Creation with OpenAI and Telegram.json](workflows/Image Creation with OpenAI and Telegram.json) |
| Image-Based Data Extraction API using Gemini AI | ai_process | httprequest, webhook, extractfromfile | 🟡 Medium | [YKZBEx4DTf0KGEBR_Image-Based_Data_Extraction_API_using_Gemini_AI.json](workflows/YKZBEx4DTf0KGEBR_Image-Based_Data_Extraction_API_using_Gemini_AI.json) |
| ImapEmail, XmlToJson, POST-HTTP-Request | ai_process | httprequest, xml, movebinarydata | 🟢 Low | [1_ImapEmail,_XmlToJson,_POST-HTTP-Request.json](workflows/1_ImapEmail,_XmlToJson,_POST-HTTP-Request.json) |
| Indeed Company Data Scraper & Summarization with Airtable, Bright Data and Google Gemini | ai_process | splitinbatches, n8n-nodes-langchain.chainllm, httprequest | 🔴 High | [TTj6BiN7bQKTa6FM_Indeed_Company_Data_Scraper_&_Summarization_with_Airtable,_Bright_Data_and_Google_Gemini.json](workflows/TTj6BiN7bQKTa6FM_Indeed_Company_Data_Scraper_&_Summarization_with_Airtable,_Bright_Data_and_Google_Gemini.json) |
| Insert and update data in Airtable | ai_process | manual, airtable | 🟢 Low | [171_Insert_and_update_data_in_Airtable.json](workflows/171_Insert_and_update_data_in_Airtable.json) |
| Integrating AI with Open-Meteo API for Enhanced Weather Forecasting | ai_process | n8n-nodes-langchain.memorybufferwindow, n8n-nodes-langchain.chat, n8n-nodes-langchain.httprequest | 🟡 Medium | [Nfh274NHoDy7pB4M_Integrating_AI_with_Open-Meteo_API_for_Enhanced_Weather_Forecasting.json](workflows/Nfh274NHoDy7pB4M_Integrating_AI_with_Open-Meteo_API_for_Enhanced_Weather_Forecasting.json) |
| Integrating AI with Open-Meteo API for Enhanced Weather Forecasting | ai_process | n8n-nodes-langchain.memorybufferwindow, n8n-nodes-langchain.chat, n8n-nodes-langchain.httprequest | 🟡 Medium | [Integrating AI with Open-Meteo API for Enhanced Weather Forecasting.json](workflows/Integrating AI with Open-Meteo API for Enhanced Weather Forecasting.json) |
| Invoice data extraction with LlamaParse and OpenAI | ai_process | n8n-nodes-langchain.chainllm, n8n-nodes-langchain.outputparserstructured, gmail | 🔴 High | [Invoice data extraction with LlamaParse and OpenAI.json](workflows/Invoice data extraction with LlamaParse and OpenAI.json) |
| Invoice data extraction with LlamaParse and OpenAI (1) | ai_process | n8n-nodes-langchain.chainllm, n8n-nodes-langchain.outputparserstructured, gmail | 🔴 High | [Invoice data extraction with LlamaParse and OpenAI (1).json](workflows/Invoice data extraction with LlamaParse and OpenAI (1).json) |
| LINE Assistant with Google Calendar and Gmail Integration | ai_process | n8n-nodes-langchain.memorybufferwindow, httprequest, googlecalendar | 🔴 High | [Z5OgwYfK4reCTv9y_LINE_Assistant_with_Google_Calendar_and_Gmail_Integration.json](workflows/Z5OgwYfK4reCTv9y_LINE_Assistant_with_Google_Calendar_and_Gmail_Integration.json) |
| LINE Assistant with Google Calendar and Gmail Integration | ai_process | n8n-nodes-langchain.memorybufferwindow, httprequest, googlecalendar | 🔴 High | [LINE Assistant with Google Calendar and Gmail Integration.json](workflows/LINE Assistant with Google Calendar and Gmail Integration.json) |
| LLM Chaining examples | ai_process | n8n-nodes-langchain.memorybufferwindow, n8n-nodes-langchain.chainllm, httprequest | 🔴 High | [43gMd18arOcxqDcC_LLM_Chaining_examples.json](workflows/43gMd18arOcxqDcC_LLM_Chaining_examples.json) |
| LangChain - Example - Code Node Example | ai_process | n8n-nodes-langchain.lmopenai, n8n-nodes-langchain.code, n8n-nodes-langchain.lmchatopenai | 🟡 Medium | [Custom LangChain agent written in JavaScript.json](workflows/Custom LangChain agent written in JavaScript.json) |
| LangChain - Example - Workflow Retriever | ai_process | n8n-nodes-langchain.chainretrievalqa, n8n-nodes-langchain.lmchatopenai, manual | 🟡 Medium | [AI_ Ask questions about any data source (using the n8n workflow retriever).json](workflows/AI_ Ask questions about any data source (using the n8n workflow retriever).json) |
| Line Chatbot Handling AI Responses with Groq and Llama3 | ai_process | webhook, httprequest | 🟡 Medium | [xibc6WDU53isYN1o_Line_Chatbot_Handling_AI_Responses_with_Groq_and_Llama3.json](workflows/xibc6WDU53isYN1o_Line_Chatbot_Handling_AI_Responses_with_Groq_and_Llama3.json) |
| LinkedIn Leads Scraping & Enrichment (Main) | ai_process | httprequest, schedule, googlesheets | 🔴 High | [7wwY8wfZdNpL83QQ_LinkedIn_Leads_Scraping_&_Enrichment_(Main).json](workflows/7wwY8wfZdNpL83QQ_LinkedIn_Leads_Scraping_&_Enrichment_(Main).json) |
| Linkedin to Airtable | ai_process | httprequest, schedule, airtable | 🟡 Medium | [ift5iHQG9G2lzJzP_Linkedin_to_Airtable.json](workflows/ift5iHQG9G2lzJzP_Linkedin_to_Airtable.json) |
| Log errors and avoid sending too many emails | ai_process | error, postgres, emailsend | 🔴 High | [YybYYc430rmZWJPJ_Log_errors_and_avoid_sending_too_many_emails.json](workflows/YybYYc430rmZWJPJ_Log_errors_and_avoid_sending_too_many_emails.json) |
| Look up a person using their email in Clearbit | ai_process | clearbit, manual | 🟢 Low | [104_Look_up_a_person_using_their_email_in_Clearbit.json](workflows/104_Look_up_a_person_using_their_email_in_Clearbit.json) |
| Luma AI - Webhook Response v1 - AK | ai_process | executiondata, webhook, airtable | 🟡 Medium | [rYuhIChQyjpGNvuR_Luma_AI_-_Webhook_Response_v1_-_AK.json](workflows/rYuhIChQyjpGNvuR_Luma_AI_-_Webhook_Response_v1_-_AK.json) |
| Luma AI Dream Machine - Simple v1 - AK | ai_process | executiondata, httprequest, manual | 🟡 Medium | [2pMoIW58KP6ZeGir_Luma_AI_Dream_Machine_-_Simple_v1_-_AK.json](workflows/2pMoIW58KP6ZeGir_Luma_AI_Dream_Machine_-_Simple_v1_-_AK.json) |
| MAIA - Health Check | ai_process | httprequest, schedule, telegram | 🟡 Medium | [wng5xcxlYA6jFS6n_MAIA_-_Health_Check.json](workflows/wng5xcxlYA6jFS6n_MAIA_-_Health_Check.json) |
| MCP_GMAIL | ai_process | gmail, n8n-nodes-langchain.mcp | 🟢 Low | [lYOQGMEJDxugrfrT_MCP_GMAIL.json](workflows/lYOQGMEJDxugrfrT_MCP_GMAIL.json) |
| Mailchimp | ai_process | mailchimp, manual | 🟢 Low | [3_Mailchimp.json](workflows/3_Mailchimp.json) |
| Make OpenAI Citation for File Retrieval RAG | ai_process | n8n-nodes-langchain.memorybufferwindow, n8n-nodes-langchain.chat, httprequest | 🔴 High | [5NAbfX550LJsfz6f_Make_OpenAI_Citation_for_File_Retrieval_RAG.json](workflows/5NAbfX550LJsfz6f_Make_OpenAI_Citation_for_File_Retrieval_RAG.json) |
| Make OpenAI Citation for File Retrieval RAG | ai_process | n8n-nodes-langchain.memorybufferwindow, n8n-nodes-langchain.chat, httprequest | 🔴 High | [Make OpenAI Citation for File Retrieval RAG.json](workflows/Make OpenAI Citation for File Retrieval RAG.json) |
| Microsoft Outlook AI Email Assistant | ai_process | splitinbatches, n8n-nodes-langchain.outputparserstructured, microsoftoutlook | 🔴 High | [Microsoft Outlook AI Email Assistant with contact support from Monday and Airtable.json](workflows/Microsoft Outlook AI Email Assistant with contact support from Monday and Airtable.json) |
| Microsoft Outlook AI Email Assistant | ai_process | splitinbatches, n8n-nodes-langchain.outputparserstructured, microsoftoutlook | 🔴 High | [reQhibpNwU63Y8sn_Microsoft_Outlook_AI_Email_Assistant.json](workflows/reQhibpNwU63Y8sn_Microsoft_Outlook_AI_Email_Assistant.json) |
| N8N Financial Tracker Telegram Invoices to Notion with AI Summaries & Reports | ai_process | editimage, n8n-nodes-langchain.chainllm, n8n-nodes-langchain.outputparserstructured | 🔴 High | [3BkxvtCbF6hHGUgM_N8N_Financial_Tracker_Telegram_Invoices_to_Notion_with_AI_Summaries_&_Reports.json](workflows/3BkxvtCbF6hHGUgM_N8N_Financial_Tracker_Telegram_Invoices_to_Notion_with_AI_Summaries_&_Reports.json) |
| Namesilo Bulk Domain Availability [Template] | ai_process | splitinbatches, httprequest, manual | 🟡 Medium | [phqg5Kk3YowxoMHQ_Namesilo_Bulk_Domain_Availability_[Template].json](workflows/phqg5Kk3YowxoMHQ_Namesilo_Bulk_Domain_Availability_[Template].json) |
| Narrating over a Video using Multimodal AI | ai_process | splitinbatches, n8n-nodes-langchain.chainllm, httprequest | 🔴 High | [Narrating over a Video using Multimodal AI.json](workflows/Narrating over a Video using Multimodal AI.json) |
| NeurochainAI Basic API Integration | ai_process | httprequest, telegram, telegram | 🔴 High | [Telegram AI Bot_ NeurochainAI Text & Image - NeurochainAI Basic API Integration.json](workflows/Telegram AI Bot_ NeurochainAI Text & Image - NeurochainAI Basic API Integration.json) |
| NeurochainAI Basic API Integration | ai_process | httprequest, telegram, telegram | 🔴 High | [RLWjEhY8L4TORAIj_NeurochainAI_Basic_API_Integration.json](workflows/RLWjEhY8L4TORAIj_NeurochainAI_Basic_API_Integration.json) |
| New OpenAI Image Generation | ai_process | httprequest, manual, converttofile | 🟡 Medium | [FyoPGDh8r3pxcGxo_New_OpenAI_Image_Generation.json](workflows/FyoPGDh8r3pxcGxo_New_OpenAI_Image_Generation.json) |
| New invoice email notification | ai_process | slack, emailsend, mindee | 🟡 Medium | [91_New_invoice_email_notification.json](workflows/91_New_invoice_email_notification.json) |
| Noco Kanban Board with AI Prioritization | ai_process | nocodb, slack, n8n-nodes-langchain.outputparserstructured | 🔴 High | [E2hq7z4ANLoL5vw1_Noco_Kanban_Board_with_AI_Prioritization.json](workflows/E2hq7z4ANLoL5vw1_Noco_Kanban_Board_with_AI_Prioritization.json) |
| Notify_user_in_Slack_of_quarantined_email_and_create_Jira_ticket_if_opened | ai_process | slack, httprequest, jira | 🔴 High | [LSH4x5nnNGQbNBkh_Notify_user_in_Slack_of_quarantined_email_and_create_Jira_ticket_if_opened.json](workflows/LSH4x5nnNGQbNBkh_Notify_user_in_Slack_of_quarantined_email_and_create_Jira_ticket_if_opened.json) |
| Notion AI Assistant Generator | ai_process | n8n-nodes-langchain.outputparserautofixing, n8n-nodes-langchain.outputparserstructured, n8n-nodes-langchain.chat | 🔴 High | [Notion AI Assistant Generator.json](workflows/Notion AI Assistant Generator.json) |
| Notion knowledge base AI assistant | ai_process | n8n-nodes-langchain.memorybufferwindow, n8n-nodes-langchain.chat, notion | 🟡 Medium | [Notion knowledge base AI assistant.json](workflows/Notion knowledge base AI assistant.json) |
| Obsidian Notes Read Aloud: Available as a Podcast Feed | ai_process | httprequest, webhook, googlesheets | 🔴 High | [Obsidian Notes Read Aloud using AI_ Available as a Podcast Feed.json](workflows/Obsidian Notes Read Aloud using AI_ Available as a Podcast Feed.json) |
| Open Deep Research - AI-Powered Autonomous Research Workflow | ai_process | splitinbatches, n8n-nodes-langchain.memorybufferwindow, n8n-nodes-langchain.chainllm | 🔴 High | [Open Deep Research - AI-Powered Autonomous Research Workflow.json](workflows/Open Deep Research - AI-Powered Autonomous Research Workflow.json) |
| Open Deep Research - AI-Powered Autonomous Research Workflow | ai_process | splitinbatches, n8n-nodes-langchain.memorybufferwindow, n8n-nodes-langchain.chainllm | 🔴 High | [WLSqXECfQF7rOj2A_Open_Deep_Research_-_AI-Powered_Autonomous_Research_Workflow.json](workflows/WLSqXECfQF7rOj2A_Open_Deep_Research_-_AI-Powered_Autonomous_Research_Workflow.json) |
| OpenAI Assistant for Hubspot Chat | ai_process | httprequest, webhook, airtable | 🔴 High | [C2pB17EpXAJwOcst_OpenAI_Assistant_for_Hubspot_Chat.json](workflows/C2pB17EpXAJwOcst_OpenAI_Assistant_for_Hubspot_Chat.json) |
| OpenAI Assistant for Hubspot Chat | ai_process | httprequest, webhook, airtable | 🔴 High | [vAssistant for Hubspot Chat using OpenAi and Airtable.json](workflows/vAssistant for Hubspot Chat using OpenAi and Airtable.json) |
| OpenAI Assistant with custom n8n tools | ai_process | n8n-nodes-langchain.openaiassistant, n8n-nodes-langchain.manualchat, n8n-nodes-langchain.code | 🔴 High | [OpenAI assistant with custom tools.json](workflows/OpenAI assistant with custom tools.json) |
| OpenAI Assistant workflow: uploa file, create an Assistant, chat with it! | ai_process | n8n-nodes-langchain.chat, manual, googledrive | 🟡 Medium | [OpenAI Assistant workflow_ upload file, create an Assistant, chat with it!.json](workflows/OpenAI Assistant workflow_ upload file, create an Assistant, chat with it!.json) |
| OpenAI ImageGen1 Template | ai_process | n8n-nodes-langchain.chat, httprequest, converttofile | 🟡 Medium | [81aN6oJGMho5kCvQ_OpenAI_ImageGen1_Template.json](workflows/81aN6oJGMho5kCvQ_OpenAI_ImageGen1_Template.json) |
| OpenAI Personal Shopper with RAG and WooCommerce | ai_process | n8n-nodes-langchain.memorybufferwindow, n8n-nodes-langchain.vectorstore, n8n-nodes-langchain.calculator | 🔴 High | [Personal Shopper Chatbot for WooCommerce with RAG using Google Drive and openAI.json](workflows/Personal Shopper Chatbot for WooCommerce with RAG using Google Drive and openAI.json) |
| OpenAI Personal Shopper with RAG and WooCommerce | ai_process | n8n-nodes-langchain.memorybufferwindow, n8n-nodes-langchain.vectorstore, n8n-nodes-langchain.calculator | 🔴 High | [fqQcmSdoVqnPeGHj_OpenAI_Personal_Shopper_with_RAG_and_WooCommerce.json](workflows/fqQcmSdoVqnPeGHj_OpenAI_Personal_Shopper_with_RAG_and_WooCommerce.json) |
| OpenAI e-mail classification - application | ai_process | n8n-nodes-langchain.textclassifier, n8n-nodes-langchain.lmchatopenai, n8n-nodes-langchain.informationextractor | 🟡 Medium | [39KuujB1fbOvx8Al_OpenAI_e-mail_classification_-_application.json](workflows/39KuujB1fbOvx8Al_OpenAI_e-mail_classification_-_application.json) |
| OpenAI-model-examples | ai_process | httprequest, readbinaryfiles, openai | 🔴 High | [OpenAI examples_ ChatGPT, DALLE-2, Whisper-1 – 5-in-1.json](workflows/OpenAI examples_ ChatGPT, DALLE-2, Whisper-1 – 5-in-1.json) |
| OpenAI-model-examples | ai_process | httprequest, readbinaryfiles, openai | 🔴 High | [147_OpenAI-model-examples.json](workflows/147_OpenAI-model-examples.json) |
| OpenAI-powered tweet generator | ai_process | httprequest, functionitem, manual | 🟢 Low | [OpenAI-powered tweet generator.json](workflows/OpenAI-powered tweet generator.json) |
| OpenSea AI-Powered Insights via Telegram | ai_process | n8n-nodes-langchain.memorybufferwindow, n8n-nodes-langchain.chat, n8n-nodes-langchain.lmchatopenai | 🔴 High | [wi2ZWKN9XPR0jkvn_OpenSea_AI-Powered_Insights_via_Telegram.json](workflows/wi2ZWKN9XPR0jkvn_OpenSea_AI-Powered_Insights_via_Telegram.json) |
| Organise Your Local File Directories With AI | ai_process | n8n-nodes-langchain.chainllm, n8n-nodes-langchain.outputparserstructured, n8n-nodes-langchain.lmchatmistralcloud | 🔴 High | [Organise Your Local File Directories With AI.json](workflows/Organise Your Local File Directories With AI.json) |
| PG&E Daily Cost Tracker | ai_process | gmail, airtop, schedule | 🔴 High | [NMGsDLoVZ7DUukGs_PG&E_Daily_Cost_Tracker.json](workflows/NMGsDLoVZ7DUukGs_PG&E_Daily_Cost_Tracker.json) |
| Parse PDF with LlamaParse and save to Airtable | ai_process | N/A | 🟢 Low | [Parse PDF with LlamaParse and save to Airtable.json](workflows/Parse PDF with LlamaParse and save to Airtable.json) |
| Perform a domain search (single) with Icypeas | ai_process | httprequest, manual | 🟢 Low | [IwOOVikQC7cn9VTv_Perform_a_domain_search_(single)_with_Icypeas.json](workflows/IwOOVikQC7cn9VTv_Perform_a_domain_search_(single)_with_Icypeas.json) |
| Perform an email search with Icypeas (single) | ai_process | httprequest, manual | 🟢 Low | [zAkPoRdcG5M5x4KT_Perform_an_email_search_with_Icypeas_(single).json](workflows/zAkPoRdcG5M5x4KT_Perform_an_email_search_with_Icypeas_(single).json) |
| Personalized AI Tech Newsletter Using RSS, OpenAI and Gmail | ai_process | n8n-nodes-langchain.vectorstoreinmemory, gmail, rssfeedread | 🔴 High | [ni6SfqC3kthAlPtX_Personalized_AI_Tech_Newsletter_Using_RSS,_OpenAI_and_Gmail.json](workflows/ni6SfqC3kthAlPtX_Personalized_AI_Tech_Newsletter_Using_RSS,_OpenAI_and_Gmail.json) |
| Proxmox AI Agent with n8n and Generative AI Integration | ai_process | n8n-nodes-langchain.outputparserautofixing, n8n-nodes-langchain.outputparserstructured, gmail | 🔴 High | [Proxmox AI Agent with n8n and Generative AI Integration.json](workflows/Proxmox AI Agent with n8n and Generative AI Integration.json) |
| Qualify new leads in Google Sheets via OpenAI's GPT-4 | ai_process | openai, googlesheets, googlesheets | 🟡 Medium | [Qualify new leads in Google Sheets via OpenAI_s GPT-4.json](workflows/Qualify new leads in Google Sheets via OpenAI_s GPT-4.json) |
| Qualify new leads in Google Sheets via OpenAI's GPT-4 | ai_process | openai, googlesheets, googlesheets | 🟡 Medium | [8FLJK1NsduFL0Y5P_Qualify_new_leads_in_Google_Sheets_via_OpenAI's_GPT-4.json](workflows/8FLJK1NsduFL0Y5P_Qualify_new_leads_in_Google_Sheets_via_OpenAI's_GPT-4.json) |
| Qualify replies from Pipedrive persons with AI | ai_process | pipedrive, gmail, openai | 🟡 Medium | [Qualify replies from Pipedrive persons with AI.json](workflows/Qualify replies from Pipedrive persons with AI.json) |
| Qualifying Appointment Requests with AI & n8n Forms | ai_process | n8n-nodes-langchain.chainllm, gmail, n8n-nodes-langchain.textclassifier | 🔴 High | [Qualifying Appointment Requests with AI & n8n Forms.json](workflows/Qualifying Appointment Requests with AI & n8n Forms.json) |
| Query Perplexity AI from your n8n workflows | ai_process | httprequest, manual | 🟢 Low | [Query Perplexity AI from your n8n workflows.json](workflows/Query Perplexity AI from your n8n workflows.json) |
| Query n8n Credentials with AI SQL Agent | ai_process | n8n-nodes-langchain.memorybufferwindow, n8n-nodes-langchain.chat, n8n-nodes-langchain.code | 🔴 High | [Query n8n Credentials with AI SQL Agent.json](workflows/Query n8n Credentials with AI SQL Agent.json) |
| RAG & GenAI App With WordPress Content | ai_process | n8n-nodes-langchain.memorypostgreschat, httprequest, postgres | 🔴 High | [o8iTqIh2sVvnuWz5_RAG_&_GenAI_App_With_WordPress_Content.json](workflows/o8iTqIh2sVvnuWz5_RAG_&_GenAI_App_With_WordPress_Content.json) |
| RAG & GenAI App With WordPress Content | ai_process | n8n-nodes-langchain.memorypostgreschat, httprequest, postgres | 🔴 High | [WordPress - AI Chatbot to enhance user experience - with Supabase and OpenAI.json](workflows/WordPress - AI Chatbot to enhance user experience - with Supabase and OpenAI.json) |
| RAG AI Agent with Milvus and Cohere | ai_process | n8n-nodes-langchain.memorybufferwindow, n8n-nodes-langchain.chat, n8n-nodes-langchain.embeddingscohere | 🔴 High | [2Eba0OHGtOmoTWOU_RAG_AI_Agent_with_Milvus_and_Cohere.json](workflows/2Eba0OHGtOmoTWOU_RAG_AI_Agent_with_Milvus_and_Cohere.json) |
| Receive a Mattermost message when new data gets added to Airtable | ai_process | airtable, mattermost | 🟢 Low | [151_Receive_a_Mattermost_message_when_new_data_gets_added_to_Airtable.json](workflows/151_Receive_a_Mattermost_message_when_new_data_gets_added_to_Airtable.json) |
| Receive updates from Telegram and send an image of a cocktail | ai_process | httprequest, telegram, telegram | 🟢 Low | [58_Receive_updates_from_Telegram_and_send_an_image_of_a_cocktail.json](workflows/58_Receive_updates_from_Telegram_and_send_an_image_of_a_cocktail.json) |
| Receive updates when a new account is added by an admin in ActiveCampaign | ai_process | activecampaign | 🟢 Low | [112_Receive_updates_when_a_new_account_is_added_by_an_admin_in_ActiveCampaign.json](workflows/112_Receive_updates_when_a_new_account_is_added_by_an_admin_in_ActiveCampaign.json) |
| Receive updates when a subscriber is added to a group and strore the information in Airtable | ai_process | mailerlite, manual, airtable | 🟢 Low | [30_Receive_updates_when_a_subscriber_is_added_to_a_group_and_strore_the_information_in_Airtable.json](workflows/30_Receive_updates_when_a_subscriber_is_added_to_a_group_and_strore_the_information_in_Airtable.json) |
| Receive updates when an email is bounced or opened | ai_process | postmark | 🟢 Low | [48_Receive_updates_when_an_email_is_bounced_or_opened.json](workflows/48_Receive_updates_when_an_email_is_bounced_or_opened.json) |
| Receive updates when an event occurs in Taiga | ai_process | taiga | 🟢 Low | [70_Receive_updates_when_an_event_occurs_in_Taiga.json](workflows/70_Receive_updates_when_an_event_occurs_in_Taiga.json) |
| Reconcile Rent Payments with Local Excel Spreadsheet and OpenAI | ai_process | n8n-nodes-langchain.outputparserstructured, readwritefile, n8n-nodes-langchain.code | 🔴 High | [Reconcile Rent Payments with Local Excel Spreadsheet and OpenAI.json](workflows/Reconcile Rent Payments with Local Excel Spreadsheet and OpenAI.json) |
| Reddit AI digest | ai_process | reddit, manual, openai | 🔴 High | [Reddit AI digest.json](workflows/Reddit AI digest.json) |
| Remove Personally Identifiable Information (PII) from CSV Files with OpenAI | ai_process | extractfromfile, googledrive, n8n-nodes-langchain.openai | 🟡 Medium | [Remove Personally Identifiable Information (PII) from CSV Files with OpenAI.json](workflows/Remove Personally Identifiable Information (PII) from CSV Files with OpenAI.json) |
| Respond to WhatsApp Messages with AI Like a Pro! | ai_process | n8n-nodes-langchain.memorybufferwindow, whatsapp, n8n-nodes-langchain.chainllm | 🔴 High | [Respond to WhatsApp Messages with AI Like a Pro!.json](workflows/Respond to WhatsApp Messages with AI Like a Pro!.json) |
| Retry on fail except for known error Template | ai_process | stopanderror, manual | 🔴 High | [qAzZekQuABuH8uho_Retry_on_fail_except_for_known_error_Template.json](workflows/qAzZekQuABuH8uho_Retry_on_fail_except_for_known_error_Template.json) |
| Scrape Books from URL with Dumpling AI, Clean HTML, Save to Sheets, Email as CSV | ai_process | gmail, httprequest, sort | 🟡 Medium | [DswhuYzoemjA6iNN_Scrape_Books_from_URL_with_Dumpling_AI,_Clean_HTML,_Save_to_Sheets,_Email_as_CSV.json](workflows/DswhuYzoemjA6iNN_Scrape_Books_from_URL_with_Dumpling_AI,_Clean_HTML,_Save_to_Sheets,_Email_as_CSV.json) |
| Scrape Web Data with Bright Data, Google Gemini and MCP Automated AI Agent | ai_process | n8n-nodes-langchain.memorybufferwindow, httprequest, readwritefile | 🔴 High | [U6cY7PPR0vaRl1I0_Scrape_Web_Data_with_Bright_Data,_Google_Gemini_and_MCP_Automated_AI_Agent.json](workflows/U6cY7PPR0vaRl1I0_Scrape_Web_Data_with_Bright_Data,_Google_Gemini_and_MCP_Automated_AI_Agent.json) |
| Scrape and summarize webpages with AI | ai_process | httprequest, n8n-nodes-langchain.chainsummarization, manual | 🔴 High | [Scrape and summarize webpages with AI.json](workflows/Scrape and summarize webpages with AI.json) |
| Search & Summarize Web Data with Perplexity, Gemini AI & Bright Data to Webhooks | ai_process | httprequest, n8n-nodes-langchain.chainsummarization, n8n-nodes-langchain.lmchatgooglegemini | 🔴 High | [ZCAkUSpaxzoRPbse_Search_&_Summarize_Web_Data_with_Perplexity,_Gemini_AI_&_Bright_Data_to_Webhooks.json](workflows/ZCAkUSpaxzoRPbse_Search_&_Summarize_Web_Data_with_Perplexity,_Gemini_AI_&_Bright_Data_to_Webhooks.json) |
| Search LinkedIn companies and add them to Airtable CRM | ai_process | splitinbatches, httprequest, manual | 🔴 High | [NOycL25YOISt8OLU_Search_LinkedIn_companies_and_add_them_to_Airtable_CRM.json](workflows/NOycL25YOISt8OLU_Search_LinkedIn_companies_and_add_them_to_Airtable_CRM.json) |
| Search LinkedIn companies, Score with AI and add them to Google Sheet CRM | ai_process | splitinbatches, httprequest, manual | 🔴 High | [GW4dTYPBXwOrCUxo_Search_LinkedIn_companies,_Score_with_AI_and_add_them_to_Google_Sheet_CRM.json](workflows/GW4dTYPBXwOrCUxo_Search_LinkedIn_companies,_Score_with_AI_and_add_them_to_Google_Sheet_CRM.json) |
| Search news using Perplexity AI and post to X (Twitter) | ai_process | schedule, httprequest, twitter | 🟢 Low | [v9K61fCQhrG6gt6Z_Search_news_using_Perplexity_AI_and_post_to_X_(Twitter).json](workflows/v9K61fCQhrG6gt6Z_Search_news_using_Perplexity_AI_and_post_to_X_(Twitter).json) |
| SearchApi AI Agent | ai_process | n8n-nodes-langchain.memorybufferwindow, n8n-nodes-langchain.chat, n8n-nodes-langchain.lmchatopenai | 🟡 Medium | [mvgpK03LMiYSiyxH_SearchApi_AI_Agent.json](workflows/mvgpK03LMiYSiyxH_SearchApi_AI_Agent.json) |
| Send Daily Birthday Reminders from Google Contacts to Slack | ai_process | slack, googlecontacts, schedule | 🟡 Medium | [9w5vu5VmXxpdBLWi_Send_Daily_Birthday_Reminders_from_Google_Contacts_to_Slack.json](workflows/9w5vu5VmXxpdBLWi_Send_Daily_Birthday_Reminders_from_Google_Contacts_to_Slack.json) |
| Send Emails from Obsidian | ai_process | splitinbatches, datetime, gmail | 🔴 High | [DNqCvzBvS7GAFWm4_Send_Emails_from_Obsidian.json](workflows/DNqCvzBvS7GAFWm4_Send_Emails_from_Obsidian.json) |
| Send SMS to numbers stored in Airtable with Twilio | ai_process | twilio, manual, airtable | 🟢 Low | [1_Send_SMS_to_numbers_stored_in_Airtable_with_Twilio.json](workflows/1_Send_SMS_to_numbers_stored_in_Airtable_with_Twilio.json) |
| Send a ChatGPT email reply and save responses to Google Sheets | ai_process | crypto, gmail, gmail | 🔴 High | [Send a ChatGPT email reply and save responses to Google Sheets.json](workflows/Send a ChatGPT email reply and save responses to Google Sheets.json) |
| Send a cocktail recipe every day via a Telegram | ai_process | httprequest, telegram, cron | 🟢 Low | [57_Send_a_cocktail_recipe_every_day_via_a_Telegram.json](workflows/57_Send_a_cocktail_recipe_every_day_via_a_Telegram.json) |
| Send an SMS when a workflow fails | ai_process | error, twilio | 🟢 Low | [56_Send_an_SMS_when_a_workflow_fails.json](workflows/56_Send_an_SMS_when_a_workflow_fails.json) |
| Send daily translated Calvin and Hobbes Comics to Discord | ai_process | httprequest, schedule, n8n-nodes-langchain.lmchatopenai | 🟡 Medium | [Send daily translated Calvin and Hobbes Comics to Discord.json](workflows/Send daily translated Calvin and Hobbes Comics to Discord.json) |
| Send daily weather updates to a phone number using the Vonage node | ai_process | openweathermap, vonage, cron | 🟢 Low | [84_Send_daily_weather_updates_to_a_phone_number_using_the_Vonage_node.json](workflows/84_Send_daily_weather_updates_to_a_phone_number_using_the_Vonage_node.json) |
| Send daily weather updates via a message in Line | ai_process | openweathermap, line, cron | 🟢 Low | [114_Send_daily_weather_updates_via_a_message_in_Line.json](workflows/114_Send_daily_weather_updates_via_a_message_in_Line.json) |
| Send daily weather updates via a message using the Gotify node | ai_process | openweathermap, gotify, cron | 🟢 Low | [115_Send_daily_weather_updates_via_a_message_using_the_Gotify_node.json](workflows/115_Send_daily_weather_updates_via_a_message_using_the_Gotify_node.json) |
| Send daily weather updates via a push notification | ai_process | openweathermap, pushover, cron | 🟢 Low | [91_Send_daily_weather_updates_via_a_push_notification.json](workflows/91_Send_daily_weather_updates_via_a_push_notification.json) |
| Send daily weather updates via a push notification using Spontit | ai_process | openweathermap, spontit, cron | 🟢 Low | [141_Send_daily_weather_updates_via_a_push_notification_using_Spontit.json](workflows/141_Send_daily_weather_updates_via_a_push_notification_using_Spontit.json) |
| Send daily weather updates via a push notification using the Pushcut node | ai_process | openweathermap, pushcut, cron | 🟢 Low | [82_Send_daily_weather_updates_via_a_push_notification_using_the_Pushcut_node.json](workflows/82_Send_daily_weather_updates_via_a_push_notification_using_the_Pushcut_node.json) |
| Send specific PDF attachments from Gmail to Google Drive using OpenAI | ai_process | gmail, openai, googledrive | 🔴 High | [Send specific PDF attachments from Gmail to Google Drive using OpenAI.json](workflows/Send specific PDF attachments from Gmail to Google Drive using OpenAI.json) |
| Send the Astronomy Picture of the day daily to a Telegram channel | ai_process | nasa, telegram, cron | 🟢 Low | [174_Send_the_Astronomy_Picture_of_the_day_daily_to_a_Telegram_channel.json](workflows/174_Send_the_Astronomy_Picture_of_the_day_daily_to_a_Telegram_channel.json) |
| Simple OpenAI Image Generator | ai_process | httprequest, form, converttofile | 🟢 Low | [AqWXpCre4fsPEkAH_Simple_OpenAI_Image_Generator.json](workflows/AqWXpCre4fsPEkAH_Simple_OpenAI_Image_Generator.json) |
| Siri AI Agent_ Apple Shortcuts powered voice template | ai_process | webhook, n8n-nodes-langchain.lmchatopenai, n8n-nodes-langchain.agent | 🟡 Medium | [Siri AI Agent_ Apple Shortcuts powered voice template.json](workflows/Siri AI Agent_ Apple Shortcuts powered voice template.json) |
| Slack AI Chatbot with RAG for company staff | ai_process | n8n-nodes-langchain.memorybufferwindow, n8n-nodes-langchain.calculator, slack | 🔴 High | [SHpLY12UobbcWRnl_Slack_AI_Chatbot_with_RAG_for_company_staff.json](workflows/SHpLY12UobbcWRnl_Slack_AI_Chatbot_with_RAG_for_company_staff.json) |
| Social Media AI Agent - Telegram | ai_process | httprequest, linkedin, markdown | 🔴 High | [ZeSJSbwXI593H1Qj_Social_Media_AI_Agent_-_Telegram.json](workflows/ZeSJSbwXI593H1Qj_Social_Media_AI_Agent_-_Telegram.json) |
| Social Media AI Agent - Telegram | ai_process | httprequest, linkedin, markdown | 🔴 High | [AI-Powered Social Media Amplifier.json](workflows/AI-Powered Social Media Amplifier.json) |
| Social Media Analysis and Automated Email Generation | ai_process | n8n-nodes-langchain.chainllm, n8n-nodes-langchain.outputparserstructured, emailsend | 🔴 High | [Social Media Analysis and Automated Email Generation.json](workflows/Social Media Analysis and Automated Email Generation.json) |
| Spot Workplace Discrimination Patterns with AI | ai_process | n8n-nodes-langchain.chainllm, quickchart, httprequest | 🔴 High | [Spot Workplace Discrimination Patterns with AI.json](workflows/Spot Workplace Discrimination Patterns with AI.json) |
| Spot Workplace Discrimination Patterns with AI | ai_process | n8n-nodes-langchain.chainllm, quickchart, httprequest | 🔴 High | [vzU9QRZsHcyRsord_Spot_Workplace_Discrimination_Patterns_with_AI.json](workflows/vzU9QRZsHcyRsord_Spot_Workplace_Discrimination_Patterns_with_AI.json) |
| Store Notion's Pages as Vector Documents into Supabase with OpenAI | ai_process | n8n-nodes-langchain.textsplittertokensplitter, n8n-nodes-langchain.vectorstoresupabase, notion | 🟡 Medium | [Store Notion_s Pages as Vector Documents into Supabase with OpenAI.json](workflows/Store Notion_s Pages as Vector Documents into Supabase with OpenAI.json) |
| Store Notion's Pages as Vector Documents into Supabase with OpenAI | ai_process | n8n-nodes-langchain.textsplittertokensplitter, n8n-nodes-langchain.vectorstoresupabase, notion | 🟡 Medium | [DvP6IHWymTIVg8Up_Store_Notion's_Pages_as_Vector_Documents_into_Supabase_with_OpenAI.json](workflows/DvP6IHWymTIVg8Up_Store_Notion's_Pages_as_Vector_Documents_into_Supabase_with_OpenAI.json) |
| Store the data received from the CocktailDB API in JSON | ai_process | writebinaryfile, httprequest, manual | 🟢 Low | [652_Store_the_data_received_from_the_CocktailDB_API_in_JSON.json](workflows/652_Store_the_data_received_from_the_CocktailDB_API_in_JSON.json) |
| Store the output of a phantom in Airtable | ai_process | phantombuster, manual, airtable | 🟢 Low | [201_Store_the_output_of_a_phantom_in_Airtable.json](workflows/201_Store_the_output_of_a_phantom_in_Airtable.json) |
| Streamline data from an n8n form into Google Sheet and Airtable | ai_process | gmail, airtable, googlesheets | 🟡 Medium | [g25bM3Hj71T3ZVVe_Streamline_data_from_an_n8n_form_into_Google_Sheet_and_Airtable.json](workflows/g25bM3Hj71T3ZVVe_Streamline_data_from_an_n8n_form_into_Google_Sheet_and_Airtable.json) |
| Summarize Google Drive Documents with Mistral AI and Send via Gmail | ai_process | gmail, n8n-nodes-langchain.chainsummarization, n8n-nodes-langchain.lmchatmistralcloud | 🟢 Low | [Jy1RMuri0WJO5aO4_Summarize_Google_Drive_Documents_with_Mistral_AI_and_Send_via_Gmail.json](workflows/Jy1RMuri0WJO5aO4_Summarize_Google_Drive_Documents_with_Mistral_AI_and_Send_via_Gmail.json) |
| Summarize Google Sheets form feedback via OpenAI's GPT-4 | ai_process | gmail, markdown, openai | 🟡 Medium | [Lwvu2jjMU2irTyAY_Summarize_Google_Sheets_form_feedback_via_OpenAI's_GPT-4.json](workflows/Lwvu2jjMU2irTyAY_Summarize_Google_Sheets_form_feedback_via_OpenAI's_GPT-4.json) |
| Summarize Google Sheets form feedback via OpenAI's GPT-4 | ai_process | gmail, markdown, openai | 🟡 Medium | [Summarize Google Sheets form feedback via OpenAI_s GPT-4.json](workflows/Summarize Google Sheets form feedback via OpenAI_s GPT-4.json) |
| Summarize emails with A.I. then send to messenger | ai_process | httprequest, emailreadimap | 🟢 Low | [Summarize your emails with A.I. (via Openrouter) and send to Line messenger.json](workflows/Summarize your emails with A.I. (via Openrouter) and send to Line messenger.json) |
| Summarize emails with A.I. then send to messenger | ai_process | httprequest, emailreadimap | 🟢 Low | [Summarize your emails with A.I. (via Openrouter) and send to Line messenger (1).json](workflows/Summarize your emails with A.I. (via Openrouter) and send to Line messenger (1).json) |
| Summarize emails with A.I. then send to messenger | ai_process | httprequest, emailreadimap | 🟢 Low | [QnVdtKiTf3nbrNkh_Summarize_emails_with_A.I._then_send_to_messenger.json](workflows/QnVdtKiTf3nbrNkh_Summarize_emails_with_A.I._then_send_to_messenger.json) |
| Sync New Files From Google Drive with Airtable | ai_process | airtable, googledrive, googledrive | 🟡 Medium | [uLHpFu2ndN6ZKClZ_Sync_New_Files_From_Google_Drive_with_Airtable.json](workflows/uLHpFu2ndN6ZKClZ_Sync_New_Files_From_Google_Drive_with_Airtable.json) |
| Telegram AI Langchain bot | ai_process | n8n-nodes-langchain.memorybufferwindow, httprequest, telegram | 🔴 High | [Telegram AI bot with LangChain nodes.json](workflows/Telegram AI bot with LangChain nodes.json) |
| Telegram AI Langchain bot | ai_process | n8n-nodes-langchain.memorybufferwindow, httprequest, telegram | 🔴 High | [ax8PJlp1UDb6EGFt_Telegram_AI_Langchain_bot.json](workflows/ax8PJlp1UDb6EGFt_Telegram_AI_Langchain_bot.json) |
| Telegram AI multi-format chatbot | ai_process | n8n-nodes-langchain.memorybufferwindow, telegram, n8n-nodes-langchain.lmchatopenai | 🔴 High | [Telegram AI bot assistant_ ready-made template for voice & text messages.json](workflows/Telegram AI bot assistant_ ready-made template for voice & text messages.json) |
| Telegram AI multi-format chatbot | ai_process | n8n-nodes-langchain.memorybufferwindow, telegram, n8n-nodes-langchain.lmchatopenai | 🔴 High | [HJwTWtzlhK8Q5SOv_Telegram_AI_multi-format_chatbot.json](workflows/HJwTWtzlhK8Q5SOv_Telegram_AI_multi-format_chatbot.json) |
| Telegram AI-bot | ai_process | telegram, openai, telegram | 🔴 High | [177_Telegram_AI-bot.json](workflows/177_Telegram_AI-bot.json) |
| Telegram AI-bot | ai_process | telegram, openai, telegram | 🔴 High | [Telegram AI Chatbot.json](workflows/Telegram AI Chatbot.json) |
| Telegram Bot with Supabase memory and OpenAI assistant integration | ai_process | supabase, httprequest, telegram | 🔴 High | [Telegram Bot with Supabase memory and OpenAI assistant integration.json](workflows/Telegram Bot with Supabase memory and OpenAI assistant integration.json) |
| Telegram-bot AI Da Nang | ai_process | n8n-nodes-langchain.memorybufferwindow, n8n-nodes-langchain.chat, telegram | 🔴 High | [bV0JTA5NtRZxiD1q_Telegram-bot_AI_Da_Nang.json](workflows/bV0JTA5NtRZxiD1q_Telegram-bot_AI_Da_Nang.json) |
| Telegram-bot AI Da Nang | ai_process | n8n-nodes-langchain.memorybufferwindow, n8n-nodes-langchain.chat, telegram | 🔴 High | [Chat with your event schedule from Google Sheets in Telegram.json](workflows/Chat with your event schedule from Google Sheets in Telegram.json) |
| Text to Speech (OpenAI) | ai_process | httprequest, manual | 🟡 Medium | [6Yzmlp5xF6oHo1VW_Text_to_Speech_(OpenAI).json](workflows/6Yzmlp5xF6oHo1VW_Text_to_Speech_(OpenAI).json) |
| Text to Speech (OpenAI) | ai_process | httprequest, manual | 🟡 Medium | [Convert text to speech with OpenAI.json](workflows/Convert text to speech with OpenAI.json) |
| The Ultimate Guide to Optimize WordPress Blog Posts with AI | ai_process | wordpress, n8n-nodes-langchain.chainllm, n8n-nodes-langchain.outputparserstructured | 🔴 High | [Mbuax8L8jEmBBYkz_The_Ultimate_Guide_to_Optimize_WordPress_Blog_Posts_with_AI.json](workflows/Mbuax8L8jEmBBYkz_The_Ultimate_Guide_to_Optimize_WordPress_Blog_Posts_with_AI.json) |
| Training Feedback Automation | ai_process | emailsend, linkedin, httprequest | 🔴 High | [pDLtBJkNSXXWSvB0_Training_Feedback_Automation.json](workflows/pDLtBJkNSXXWSvB0_Training_Feedback_Automation.json) |
| Transcribing Bank Statements To Markdown Using Gemini Vision AI | ai_process | n8n-nodes-langchain.chainllm, httprequest, sort | 🔴 High | [Transcribing Bank Statements To Markdown Using Gemini Vision AI.json](workflows/Transcribing Bank Statements To Markdown Using Gemini Vision AI.json) |
| Translate Telegram audio messages with AI (55 supported languages) v1 | ai_process | n8n-nodes-langchain.chainllm, n8n-nodes-langchain.lmchatopenai, telegram | 🟡 Medium | [IvgAFAUOSI3biT4L_Translate_Telegram_audio_messages_with_AI_(55_supported_languages)_v1.json](workflows/IvgAFAUOSI3biT4L_Translate_Telegram_audio_messages_with_AI_(55_supported_languages)_v1.json) |
| Translate Telegram audio messages with AI (55 supported languages) v1 | ai_process | n8n-nodes-langchain.chainllm, n8n-nodes-langchain.lmchatopenai, telegram | 🟡 Medium | [Translate Telegram audio messages with AI (55 supported languages).json](workflows/Translate Telegram audio messages with AI (55 supported languages).json) |
| Translate audio using AI | ai_process | n8n-nodes-langchain.chainllm, httprequest, n8n-nodes-langchain.lmchatopenai | 🟡 Medium | [Translate audio using AI.json](workflows/Translate audio using AI.json) |
| Translate cocktail instructions using LingvaNex | ai_process | httprequest, manual, lingvanex | 🟢 Low | [145_Translate_cocktail_instructions_using_LingvaNex.json](workflows/145_Translate_cocktail_instructions_using_LingvaNex.json) |
| Translate questions about e-mails into SQL queries and run them | ai_process | postgres, n8n-nodes-langchain.chat, readwritefile | 🔴 High | [AC4paL1SXMFURgmc_Translate_questions_about_e-mails_into_SQL_queries_and_run_them.json](workflows/AC4paL1SXMFURgmc_Translate_questions_about_e-mails_into_SQL_queries_and_run_them.json) |
| Travel Planning Agent with Couchbase Vector Search, Gemini 2.0 Flash and OpenAI | ai_process | n8n-nodes-langchain.memorybufferwindow, n8n-nodes-langchain.chat, n8n-nodes-langchain.embeddingsopenai | 🔴 High | [iGAzT789R7Q1fOOE_Travel_Planning_Agent_with_Couchbase_Vector_Search,_Gemini_2.0_Flash_and_OpenAI.json](workflows/iGAzT789R7Q1fOOE_Travel_Planning_Agent_with_Couchbase_Vector_Search,_Gemini_2.0_Flash_and_OpenAI.json) |
| Twitter Virtual AI Influencer | ai_process | schedule, manual, n8n-nodes-langchain.openai | 🟡 Medium | [Twitter Virtual AI Influencer.json](workflows/Twitter Virtual AI Influencer.json) |
| Unsubscribe Mautic contacts from automated unsubscribe emails | ai_process | gmail, gmail, mautic | 🔴 High | [2241_Unsubscribe_Mautic_contacts_from_automated_unsubscribe_emails.json](workflows/2241_Unsubscribe_Mautic_contacts_from_automated_unsubscribe_emails.json) |
| Use AI to organize your Todoist Inbox | ai_process | schedule, todoist, n8n-nodes-langchain.openai | 🟡 Medium | [Use AI to organize your Todoist Inbox.json](workflows/Use AI to organize your Todoist Inbox.json) |
| Very simple Human in the loop system email with AI e IMAP | ai_process | emailsend, n8n-nodes-langchain.chainsummarization, markdown | 🔴 High | [A Very Simple _Human in the Loop_ Email Response System Using AI and IMAP.json](workflows/A Very Simple _Human in the Loop_ Email Response System Using AI and IMAP.json) |
| Very simple Human in the loop system email with AI e IMAP | ai_process | emailsend, n8n-nodes-langchain.chainsummarization, markdown | 🔴 High | [Nvn78tMRNnKji7Fg_Very_simple_Human_in_the_loop_system_email_with_AI_e_IMAP.json](workflows/Nvn78tMRNnKji7Fg_Very_simple_Human_in_the_loop_system_email_with_AI_e_IMAP.json) |
| Vision-Based AI Agent Scraper - with Google Sheets, ScrapingBee, and Gemini | ai_process | n8n-nodes-langchain.outputparserstructured, httprequest, markdown | 🔴 High | [✨ Vision-Based AI Agent Scraper - with Google Sheets, ScrapingBee, and Gemini.json](workflows/✨ Vision-Based AI Agent Scraper - with Google Sheets, ScrapingBee, and Gemini.json) |
| Vision-Based AI Agent Scraper - with Google Sheets, ScrapingBee, and Gemini | ai_process | n8n-nodes-langchain.outputparserstructured, httprequest, markdown | 🔴 High | [PpFVCrTiYoa35q1m_Vision-Based_AI_Agent_Scraper_-_with_Google_Sheets,_ScrapingBee,_and_Gemini.json](workflows/PpFVCrTiYoa35q1m_Vision-Based_AI_Agent_Scraper_-_with_Google_Sheets,_ScrapingBee,_and_Gemini.json) |
| Visual Regression Testing with Apify and AI Vision Model | ai_process | splitinbatches, n8n-nodes-langchain.chainllm, n8n-nodes-langchain.outputparserstructured | 🔴 High | [Visual Regression Testing with Apify and AI Vision Model.json](workflows/Visual Regression Testing with Apify and AI Vision Model.json) |
| Visualize your SQL Agent queries with OpenAI and Quickchart.io | ai_process | n8n-nodes-langchain.memorybufferwindow, n8n-nodes-langchain.chat, httprequest | 🔴 High | [Visualize your SQL Agent queries with OpenAI and Quickchart.io.json](workflows/Visualize your SQL Agent queries with OpenAI and Quickchart.io.json) |
| Voice RAG Chatbot with ElevenLabs and OpenAI | ai_process | n8n-nodes-langchain.memorybufferwindow, n8n-nodes-langchain.vectorstore, n8n-nodes-langchain.textsplittertokensplitter | 🔴 High | [ibiHg6umCqvcTF4g_Voice_RAG_Chatbot_with_ElevenLabs_and_OpenAI.json](workflows/ibiHg6umCqvcTF4g_Voice_RAG_Chatbot_with_ElevenLabs_and_OpenAI.json) |
| Voice RAG Chatbot with ElevenLabs and OpenAI | ai_process | n8n-nodes-langchain.memorybufferwindow, n8n-nodes-langchain.vectorstore, n8n-nodes-langchain.textsplittertokensplitter | 🔴 High | [AI Voice Chatbot with ElevenLabs & OpenAI for Customer Service and Restaurants.json](workflows/AI Voice Chatbot with ElevenLabs & OpenAI for Customer Service and Restaurants.json) |
| WooCommerce AI Chatbot Workflow for Post-Sales Support | ai_process | telegram, httprequest, googledrive | 🔴 High | [ODZpSQqCxkISEqv8_WooCommerce_AI_Chatbot_Workflow_for_Post-Sales_Support.json](workflows/ODZpSQqCxkISEqv8_WooCommerce_AI_Chatbot_Workflow_for_Post-Sales_Support.json) |
| Workflow dashboard with mermaid.js | ai_process | webhook, manual, n8n | 🔴 High | [Um37boya1U0mnCjS_Workflow_dashboard_with_mermaid.js.json](workflows/Um37boya1U0mnCjS_Workflow_dashboard_with_mermaid.js.json) |
| Write a WordPress post with AI (starting from a few keywords) | ai_process | wordpress, respondtowebhook, httprequest | 🔴 High | [Write a WordPress post with AI (starting from a few keywords).json](workflows/Write a WordPress post with AI (starting from a few keywords).json) |
| YT AI News Playlist Creator/AI News Form Updater | ai_process | httprequest, schedule, manual | 🔴 High | [2LFEJVoSkeZMndiM_YT_AI_News_Playlist_Creator_AI_News_Form_Updater.json](workflows/2LFEJVoSkeZMndiM_YT_AI_News_Playlist_Creator_AI_News_Form_Updater.json) |
| YogiAI | ai_process | n8n-nodes-langchain.outputparserautofixing, n8n-nodes-langchain.lmchatazureopenai, n8n-nodes-langchain.chainllm | 🔴 High | [2DzQ1FH11S3Gp6wn_YogiAI.json](workflows/2DzQ1FH11S3Gp6wn_YogiAI.json) |
| YouTube Videos with AI Summaries on Discord | ai_process | rssfeedread, httprequest, extractfromfile | 🟡 Medium | [Share YouTube Videos with AI Summaries on Discord.json](workflows/Share YouTube Videos with AI Summaries on Discord.json) |
| YouTube Videos with AI Summaries on Discord | ai_process | rssfeedread, httprequest, extractfromfile | 🟡 Medium | [LF8gz3iz74u45a5i_YouTube_Videos_with_AI_Summaries_on_Discord.json](workflows/LF8gz3iz74u45a5i_YouTube_Videos_with_AI_Summaries_on_Discord.json) |
| YouTube to Airtable Anonym | ai_process | httprequest, schedule, n8n-nodes-langchain.informationextractor | 🟡 Medium | [6bMVzmrbPexvBe6q_YouTube_to_Airtable_Anonym.json](workflows/6bMVzmrbPexvBe6q_YouTube_to_Airtable_Anonym.json) |
| YouTube to Raindrop | ai_process | functionitem, manual, cron | 🟡 Medium | [7_YouTube_to_Raindrop.json](workflows/7_YouTube_to_Raindrop.json) |
| Zoom AI Meeting Assistant | ai_process | clickup, httprequest, n8n-nodes-langchain.lmchatanthropic | 🔴 High | [jhNsy4dPQYw9QDaa_Zoom_AI_Meeting_Assistant.json](workflows/jhNsy4dPQYw9QDaa_Zoom_AI_Meeting_Assistant.json) |
| Zoom AI Meeting Assistant | ai_process | clickup, httprequest, extractfromfile | 🔴 High | [Zoom AI Meeting Assistant creates mail summary, ClickUp tasks and follow-up call.json](workflows/Zoom AI Meeting Assistant creates mail summary, ClickUp tasks and follow-up call.json) |
| [AI/LangChain] Output Parser 4 | ai_process | n8n-nodes-langchain.outputparserautofixing, n8n-nodes-langchain.chainllm, n8n-nodes-langchain.outputparserstructured | 🟡 Medium | [Force AI to use a specific output format.json](workflows/Force AI to use a specific output format.json) |
| airflow dag_run | ai_process | httprequest, stopanderror, executeworkflow | 🟡 Medium | [Y5URlIlbX4HDzWKA_airflow_dag_run.json](workflows/Y5URlIlbX4HDzWKA_airflow_dag_run.json) |
| chrome extension backend with AI | ai_process | webhook, n8n-nodes-langchain.openai, respondtowebhook | 🟢 Low | [Q8On8rR6BkmPzDUd_chrome_extension_backend_with_AI.json](workflows/Q8On8rR6BkmPzDUd_chrome_extension_backend_with_AI.json) |
| chrome extension backend with AI | ai_process | webhook, n8n-nodes-langchain.openai, respondtowebhook | 🟢 Low | [Analyze tradingview.com charts with Chrome extension, N8N and OpenAI.json](workflows/Analyze tradingview.com charts with Chrome extension, N8N and OpenAI.json) |
| create e-mail responses with fastmail and OpenAI | ai_process | httprequest, n8n-nodes-langchain.openai, emailreadimap | 🟡 Medium | [create e-mail responses with fastmail and OpenAI.json](workflows/create e-mail responses with fastmail and OpenAI.json) |
| e-mail Chatbot with both semantic and structured RAG, using Telegram and Pgvector | ai_process | splitinbatches, n8n-nodes-langchain.memorybufferwindow, n8n-nodes-langchain.chat | 🔴 High | [LPQsiqt476n7ne7f_e-mail_Chatbot_with_both_semantic_and_structured_RAG,_using_Telegram_and_Pgvector.json](workflows/LPQsiqt476n7ne7f_e-mail_Chatbot_with_both_semantic_and_structured_RAG,_using_Telegram_and_Pgvector.json) |
| mails2notion V2 | ai_process | n8n-nodes-langchain.calculator, n8n-nodes-langchain.outputparserstructured, gmail | 🔴 High | [30r9acI1XVIIwAMi_mails2notion_V2.json](workflows/30r9acI1XVIIwAMi_mails2notion_V2.json) |
| mails2notion V2 | ai_process | n8n-nodes-langchain.calculator, n8n-nodes-langchain.outputparserstructured, gmail | 🔴 High | [Turn Emails into AI-Enhanced Tasks in Notion (Multi-User Support) with Gmail, Airtable and Softr.json](workflows/Turn Emails into AI-Enhanced Tasks in Notion (Multi-User Support) with Gmail, Airtable and Softr.json) |
| verify email | ai_process | functionitem, uproc, manual | 🟢 Low | [103_verify_email.json](workflows/103_verify_email.json) |
| xSend and check TTS (Text-to-speech) voice calls end email verification | ai_process | emailsend, httprequest, form | 🔴 High | [1g8EAij2RwhNN70t_xSend_and_check_TTS_(Text-to-speech)_voice_calls_end_email_verification.json](workflows/1g8EAij2RwhNN70t_xSend_and_check_TTS_(Text-to-speech)_voice_calls_end_email_verification.json) |
| ↔️ Airtable Batch Processing | ai_process | splitinbatches, httprequest, manual | 🔴 High | [121pu6oiTjzkJ8OT_↔️_Airtable_Batch_Processing.json](workflows/121pu6oiTjzkJ8OT_↔️_Airtable_Batch_Processing.json) |
| ⚡AI-Powered YouTube Playlist & Video Summarization and Analysis v2 | ai_process | n8n-nodes-langchain.outputparserstructured, httprequest, redis | 🔴 High | [4Tq5HZBdETVe7jEb_⚡AI-Powered_YouTube_Playlist_&_Video_Summarization_and_Analysis_v2.json](workflows/4Tq5HZBdETVe7jEb_⚡AI-Powered_YouTube_Playlist_&_Video_Summarization_and_Analysis_v2.json) |
| ⚡AI-Powered YouTube Video Summarization & Analysis | ai_process | n8n-nodes-langchain.chainllm, youtube, webhook | 🔴 High | [⚡AI-Powered YouTube Video Summarization & Analysis.json](workflows/⚡AI-Powered YouTube Video Summarization & Analysis.json) |
| ⚡📽️ Ultimate AI-Powered Chatbot for YouTube Summarization & Analysis | ai_process | n8n-nodes-langchain.memorybufferwindow, n8n-nodes-langchain.chat, httprequest | 🔴 High | [GM9Qxzul4NPQpJkn_⚡📽️_Ultimate_AI-Powered_Chatbot_for_YouTube_Summarization_&_Analysis.json](workflows/GM9Qxzul4NPQpJkn_⚡📽️_Ultimate_AI-Powered_Chatbot_for_YouTube_Summarization_&_Analysis.json) |
| ✨📊Multi-AI Agent Chatbot for Postgres/Supabase DB and QuickCharts + Tool Router | ai_process | n8n-nodes-langchain.memorypostgreschat, n8n-nodes-langchain.outputparserstructured, n8n-nodes-langchain.chat | 🔴 High | [Q63cSgFlcqz291ec_✨📊Multi-AI_Agent_Chatbot_for_Postgres_Supabase_DB_and_QuickCharts_+_Tool_Router.json](workflows/Q63cSgFlcqz291ec_✨📊Multi-AI_Agent_Chatbot_for_Postgres_Supabase_DB_and_QuickCharts_+_Tool_Router.json) |
| ✨🔪 Advanced AI Powered Document Parsing & Text Extraction with Llama Parse | ai_process | n8n-nodes-langchain.chainllm, gmail, gmail | 🔴 High | [kjyWJWfDlyXkKL3m_✨🔪_Advanced_AI_Powered_Document_Parsing_&_Text_Extraction_with_Llama_Parse.json](workflows/kjyWJWfDlyXkKL3m_✨🔪_Advanced_AI_Powered_Document_Parsing_&_Text_Extraction_with_Llama_Parse.json) |
| 🌐 Confluence Page AI Powered Chatbot | ai_process | n8n-nodes-langchain.memorybufferwindow, httprequest, markdown | 🔴 High | [mOcaSIUAvpt3QjQ1_🌐_Confluence_Page_AI_Powered_Chatbot.json](workflows/mOcaSIUAvpt3QjQ1_🌐_Confluence_Page_AI_Powered_Chatbot.json) |
| 🌐🪛 AI Agent Chatbot with Jina.ai Webpage Scraper | ai_process | n8n-nodes-langchain.memorybufferwindow, n8n-nodes-langchain.chat, n8n-nodes-langchain.httprequest | 🟡 Medium | [xEij0kj2I1DHbL3I_🌐🪛_AI_Agent_Chatbot_with_Jina.ai_Webpage_Scraper.json](workflows/xEij0kj2I1DHbL3I_🌐🪛_AI_Agent_Chatbot_with_Jina.ai_Webpage_Scraper.json) |
| 🎥 Gemini AI Video Analysis | ai_process | httprequest, manual | 🟡 Medium | [hKkZYhJqBNir8amQ_🎥_Gemini_AI_Video_Analysis.json](workflows/hKkZYhJqBNir8amQ_🎥_Gemini_AI_Video_Analysis.json) |
| 🐋🤖 DeepSeek AI Agent + Telegram + LONG TERM Memory 🧠 | ai_process | n8n-nodes-langchain.memorybufferwindow, n8n-nodes-langchain.chat, googledocs | 🔴 High | [rtsvydad1MOCryia_🐋🤖_DeepSeek_AI_Agent_+_Telegram_+_LONG_TERM_Memory_🧠.json](workflows/rtsvydad1MOCryia_🐋🤖_DeepSeek_AI_Agent_+_Telegram_+_LONG_TERM_Memory_🧠.json) |
| 🐋🤖 DeepSeek AI Agent + Telegram + LONG TERM Memory 🧠 | ai_process | n8n-nodes-langchain.memorybufferwindow, n8n-nodes-langchain.chat, googledocs | 🔴 High | [🐋🤖 DeepSeek AI Agent + Telegram + LONG TERM Memory 🧠.json](workflows/🐋🤖 DeepSeek AI Agent + Telegram + LONG TERM Memory 🧠.json) |
| 💡🌐 Essential Multipage Website Scraper with Jina.ai | ai_process | splitinbatches, httprequest, manual | 🔴 High | [xEij0kj2I1DHbL3I_💡🌐_Essential_Multipage_Website_Scraper_with_Jina.ai.json](workflows/xEij0kj2I1DHbL3I_💡🌐_Essential_Multipage_Website_Scraper_with_Jina.ai.json) |
| 💥AI Social Video Generator with GPT-4, Kling & Blotato —Auto-Post to Instagram, Facebook,, TikTok, Twitter & Pinterest - vide | ai_process | httprequest, n8n-nodes-langchain.lmchatopenai, telegram | 🔴 High | [SvZQB2gsI57KlfvO_💥AI_Social_Video_Generator_with_GPT-4,_Kling_&_Blotato_—Auto-Post_to_Instagram,_Facebook,,_TikTok,_Twitter_&_Pinterest_-_vide.json](workflows/SvZQB2gsI57KlfvO_💥AI_Social_Video_Generator_with_GPT-4,_Kling_&_Blotato_—Auto-Post_to_Instagram,_Facebook,,_TikTok,_Twitter_&_Pinterest_-_vide.json) |
| 📄✨ Easy Wordpress Content Creation from PDF Document + Human In The Loop with Gmail Approval | ai_process | wordpress, n8n-nodes-langchain.chainllm, gmail | 🔴 High | [fSG22q8TeUtsGUGD_📄✨_Easy_Wordpress_Content_Creation_from_PDF_Document_+_Human_In_The_Loop_with_Gmail_Approval.json](workflows/fSG22q8TeUtsGUGD_📄✨_Easy_Wordpress_Content_Creation_from_PDF_Document_+_Human_In_The_Loop_with_Gmail_Approval.json) |
| 📈 Receive Daily Market News from FT.com to your Microsoft outlook inbox | ai_process | httprequest, microsoftoutlook, schedule | 🟡 Medium | [📈 Receive Daily Market News from FT.com to your Microsoft outlook inbox.json](workflows/📈 Receive Daily Market News from FT.com to your Microsoft outlook inbox.json) |
| 📦 New Email ➔ Create Google Task | ai_process | gmail, googletasks | 🟢 Low | [z0C6H2kYSgML2dib_📦_New_Email_➔_Create_Google_Task.json](workflows/z0C6H2kYSgML2dib_📦_New_Email_➔_Create_Google_Task.json) |
| 🔍 Perplexity Research to HTML_ AI-Powered Content Creation | ai_process | N/A | 🟢 Low | [🔍 Perplexity Research to HTML_ AI-Powered Content Creation.json](workflows/🔍 Perplexity Research to HTML_ AI-Powered Content Creation.json) |
| 🔥📈🤖 AI Agent  for n8n Creators Leaderboard - Find Popular Workflows | ai_process | n8n-nodes-langchain.memorybufferwindow, n8n-nodes-langchain.chat, httprequest | 🔴 High | [b8a4IwiwD9SlgF42_🔥📈🤖_AI_Agent__for_n8n_Creators_Leaderboard_-_Find_Popular_Workflows.json](workflows/b8a4IwiwD9SlgF42_🔥📈🤖_AI_Agent__for_n8n_Creators_Leaderboard_-_Find_Popular_Workflows.json) |
| 🔥📈🤖 AI Agent for n8n Creators Leaderboard - Find Popular Workflows | ai_process | n8n-nodes-langchain.memorybufferwindow, n8n-nodes-langchain.chat, httprequest | 🔴 High | [🔥📈🤖 AI Agent for n8n Creators Leaderboard - Find Popular Workflows.json](workflows/🔥📈🤖 AI Agent for n8n Creators Leaderboard - Find Popular Workflows.json) |
| 🤖 AI Powered RAG Chatbot for Your Docs + Google Drive + Gemini + Qdrant | ai_process | n8n-nodes-langchain.informationextractor, extractfromfile, googledrive | 🔴 High | [8tusZTTtcyaiznEG_🤖_AI_Powered_RAG_Chatbot_for_Your_Docs_+_Google_Drive_+_Gemini_+_Qdrant.json](workflows/8tusZTTtcyaiznEG_🤖_AI_Powered_RAG_Chatbot_for_Your_Docs_+_Google_Drive_+_Gemini_+_Qdrant.json) |
| 🤖Email Agent | ai_process | n8n-nodes-langchain.lmchatopenai, n8n-nodes-langchain.agent, gmail | 🟡 Medium | [__Email_Agent.json](workflows/__Email_Agent.json) |
| 🤖🧑‍💻 AI Agent  for Top n8n Creators Leaderboard Reporting | ai_process | httprequest, sort, googledrive | 🔴 High | [6zSE618gr9fDtAfF_🤖🧑‍💻_AI_Agent__for_Top_n8n_Creators_Leaderboard_Reporting.json](workflows/6zSE618gr9fDtAfF_🤖🧑‍💻_AI_Agent__for_Top_n8n_Creators_Leaderboard_Reporting.json) |
| 🤖🧑‍💻 AI Agent for Top n8n Creators Leaderboard Reporting | ai_process | httprequest, sort, googledrive | 🔴 High | [🤖🧑_💻 AI Agent for Top n8n Creators Leaderboard Reporting.json](workflows/🤖🧑_💻 AI Agent for Top n8n Creators Leaderboard Reporting.json) |
| 🤖🧠 AI Agent Chatbot + LONG TERM Memory + Note Storage + Telegram | ai_process | n8n-nodes-langchain.memorybufferwindow, n8n-nodes-langchain.chat, googledocs | 🔴 High | [🤖🧠 AI Agent Chatbot + LONG TERM Memory + Note Storage + Telegram.json](workflows/🤖🧠 AI Agent Chatbot + LONG TERM Memory + Note Storage + Telegram.json) |
| 🤖🧠 AI Agent Chatbot + LONG TERM Memory + Note Storage + Telegram | ai_process | n8n-nodes-langchain.memorybufferwindow, n8n-nodes-langchain.chat, googledocs | 🔴 High | [QJZLBn9L6NbmjmLK_🤖🧠_AI_Agent_Chatbot_+_LONG_TERM_Memory_+_Note_Storage_+_Telegram.json](workflows/QJZLBn9L6NbmjmLK_🤖🧠_AI_Agent_Chatbot_+_LONG_TERM_Memory_+_Note_Storage_+_Telegram.json) |
| 🦜✨Use OpenAI to Transcribe Audio + Summarize with AI + Save to Google Drive | ai_process | gmail, googledrive, manual | 🔴 High | [CNOMivCLJRGfZnUM_🦜✨Use_OpenAI_to_Transcribe_Audio_+_Summarize_with_AI_+_Save_to_Google_Drive.json](workflows/CNOMivCLJRGfZnUM_🦜✨Use_OpenAI_to_Transcribe_Audio_+_Summarize_with_AI_+_Save_to_Google_Drive.json) |
| 🧠 Give Your AI Agent Chatbot Long Term Memory Tools Router | ai_process | n8n-nodes-langchain.memorybufferwindow, n8n-nodes-langchain.chainllm, gmail | 🔴 High | [p7xESnT1xMZD2hRk_🧠_Give_Your_AI_Agent_Chatbot_Long_Term_Memory_Tools_Router.json](workflows/p7xESnT1xMZD2hRk_🧠_Give_Your_AI_Agent_Chatbot_Long_Term_Memory_Tools_Router.json) |
| AI Agent to chat with Airtable and analyze data | analyze | N/A | 🟢 Low | [AI Agent to chat with Airtable and analyze data.json](workflows/AI Agent to chat with Airtable and analyze data.json) |
| AI Customer feedback sentiment analysis | analyze | openai, googlesheets, form | 🟡 Medium | [AI Customer feedback sentiment analysis.json](workflows/AI Customer feedback sentiment analysis.json) |
| Analyze & Sort Suspicious Email Contents with ChatGPT | analyze | gmail, httprequest, jira | 🔴 High | [Analyze & Sort Suspicious Email Contents with ChatGPT.json](workflows/Analyze & Sort Suspicious Email Contents with ChatGPT.json) |
| Analyze Reddit Posts with AI to Identify Business Opportunities | analyze | reddit, gmail, n8n-nodes-langchain.chainsummarization | 🔴 High | [Xx4zOjRFLI8W9PiC_Analyze_Reddit_Posts_with_AI_to_Identify_Business_Opportunities.json](workflows/Xx4zOjRFLI8W9PiC_Analyze_Reddit_Posts_with_AI_to_Identify_Business_Opportunities.json) |
| Analyze Screenshots with AI | analyze | httprequest, manual, n8n-nodes-langchain.openai | 🟡 Medium | [wDD4XugmHIvx3KMT_Analyze_Screenshots_with_AI.json](workflows/wDD4XugmHIvx3KMT_Analyze_Screenshots_with_AI.json) |
| Analyze Screenshots with AI | analyze | httprequest, manual, n8n-nodes-langchain.openai | 🟡 Medium | [Automate Screenshots with URLbox & Analyze them with AI.json](workflows/Automate Screenshots with URLbox & Analyze them with AI.json) |
| Analyze Suspicious Email Contents with ChatGPT Vision | analyze | gmail, httprequest, jira | 🔴 High | [Analyze Suspicious Email Contents with ChatGPT Vision.json](workflows/Analyze Suspicious Email Contents with ChatGPT Vision.json) |
| Analyze a URL and get the job details using the Cortex node | analyze | cortex, manual | 🟢 Low | [160_Analyze_a_URL_and_get_the_job_details_using_the_Cortex_node.json](workflows/160_Analyze_a_URL_and_get_the_job_details_using_the_Cortex_node.json) |
| Analyze_email_headers_for_IPs_and_spoofing__3 | analyze | itemlists, httprequest, webhook | 🔴 High | [3tJcVzt2OqeyjfnH_Analyze_email_headers_for_IPs_and_spoofing__3.json](workflows/3tJcVzt2OqeyjfnH_Analyze_email_headers_for_IPs_and_spoofing__3.json) |
| Brand Content Extract, Summarize & Sentiment Analysis with Bright Data | analyze | n8n-nodes-langchain.chainllm, httprequest, n8n-nodes-langchain.chainsummarization | 🔴 High | [wTI77cpLkbxsRQat_Brand_Content_Extract,_Summarize_&_Sentiment_Analysis_with_Bright_Data.json](workflows/wTI77cpLkbxsRQat_Brand_Content_Extract,_Summarize_&_Sentiment_Analysis_with_Bright_Data.json) |
| Crypto News & Sentiment | analyze | rssfeedread, n8n-nodes-langchain.lmchatopenai, telegram | 🔴 High | [8v4dynjkHSLVGJSG_Crypto_News_&_Sentiment.json](workflows/8v4dynjkHSLVGJSG_Crypto_News_&_Sentiment.json) |
| Receive_and_analyze_emails_with_rules_in_Sublime_Security | analyze | slack, httprequest, manual | 🔴 High | [84KL1bsi9OvbAapn_Receive_and_analyze_emails_with_rules_in_Sublime_Security.json](workflows/84KL1bsi9OvbAapn_Receive_and_analyze_emails_with_rules_in_Sublime_Security.json) |
| Scrape Trustpilot Reviews with DeepSeek, Analyze Sentiment with OpenAI | analyze | httprequest, manual, n8n-nodes-langchain.informationextractor | 🔴 High | [w434EiZ2z7klQAyp_Scrape_Trustpilot_Reviews_with_DeepSeek,_Analyze_Sentiment_with_OpenAI.json](workflows/w434EiZ2z7klQAyp_Scrape_Trustpilot_Reviews_with_DeepSeek,_Analyze_Sentiment_with_OpenAI.json) |
| Scrape Trustpilot Reviews with DeepSeek, Analyze Sentiment with OpenAI | analyze | httprequest, manual, n8n-nodes-langchain.informationextractor | 🔴 High | [Scrape Trustpilot Reviews with DeepSeek, Analyze Sentiment with OpenAI.json](workflows/Scrape Trustpilot Reviews with DeepSeek, Analyze Sentiment with OpenAI.json) |
| Sentiment Analysis Tracking on Support Issues with Linear and Slack | analyze | splitinbatches, removeduplicates, slack | 🔴 High | [Sentiment Analysis Tracking on Support Issues with Linear and Slack.json](workflows/Sentiment Analysis Tracking on Support Issues with Linear and Slack.json) |
| Sentiment Analysis Tracking on Support Issues with Linear and Slack (1) | analyze | splitinbatches, removeduplicates, slack | 🔴 High | [Sentiment Analysis Tracking on Support Issues with Linear and Slack (1).json](workflows/Sentiment Analysis Tracking on Support Issues with Linear and Slack (1).json) |
| YouTube Comment Sentiment Analyzer | analyze | httprequest, n8n-nodes-langchain.lmchatopenai, manual | 🔴 High | [xaC6zL4bWBo14xyJ_YouTube_Comment_Sentiment_Analyzer.json](workflows/xaC6zL4bWBo14xyJ_YouTube_Comment_Sentiment_Analyzer.json) |
| YouTube Video Analyzer with AI | analyze | n8n-nodes-langchain.lmchatdeepseek, n8n-nodes-langchain.chainllm, n8n-nodes-langchain.outputparserstructured | 🔴 High | [G3yjjk93c1bBM5tc_YouTube_Video_Analyzer_with_AI.json](workflows/G3yjjk93c1bBM5tc_YouTube_Video_Analyzer_with_AI.json) |
| 🎥 Analyze YouTube Video for Summaries, Transcripts & Content + Google Gemini AI | analyze | gmail, httprequest, markdown | 🔴 High | [LIAes1kWVZAWZBX2_🎥_Analyze_YouTube_Video_for_Summaries,_Transcripts_&_Content_+_Google_Gemini_AI.json](workflows/LIAes1kWVZAWZBX2_🎥_Analyze_YouTube_Video_for_Summaries,_Transcripts_&_Content_+_Google_Gemini_AI.json) |
| (G) LineChatBot + Google Sheets (as a memory) | automate | httprequest, webhook, n8n-nodes-langchain.lmchatgooglegemini | 🔴 High | [[CENSORED]_(G)_LineChatBot_+_Google_Sheets_(as_a_memory).json](workflows/[CENSORED]_(G)_LineChatBot_+_Google_Sheets_(as_a_memory).json) |
| 1838_workflow_1838 | automate | hubspot, slack, lemlist | 🟡 Medium | [1838_workflow_1838.json](workflows/1838_workflow_1838.json) |
| 1862_workflow_1862 | automate | splitinbatches, htmlextract, httprequest | 🟡 Medium | [1862_workflow_1862.json](workflows/1862_workflow_1862.json) |
| 1895_workflow_1895 | automate | reddit, manual, openai | 🔴 High | [1895_workflow_1895.json](workflows/1895_workflow_1895.json) |
| 1897_workflow_1897 | automate | gmail, openai, googledrive | 🔴 High | [1897_workflow_1897.json](workflows/1897_workflow_1897.json) |
| 1898_workflow_1898 | automate | crypto, gmail, gmail | 🔴 High | [1898_workflow_1898.json](workflows/1898_workflow_1898.json) |
| 1951_workflow_1951 | automate | httprequest, n8n-nodes-langchain.chainsummarization, n8n-nodes-langchain.lmchatopenai | 🔴 High | [1951_workflow_1951.json](workflows/1951_workflow_1951.json) |
| 1953_workflow_1953 | automate | gmail, gmail, n8n-nodes-langchain.textclassifier | 🟡 Medium | [1953_workflow_1953.json](workflows/1953_workflow_1953.json) |
| 1954_workflow_1954 | automate | n8n-nodes-langchain.memorybufferwindow, n8n-nodes-langchain.chat, n8n-nodes-langchain.lmchatopenai | 🟢 Low | [1954_workflow_1954.json](workflows/1954_workflow_1954.json) |
| 1955_workflow_1955 | automate | n8n-nodes-langchain.code, n8n-nodes-langchain.lmchatopenai, manual | 🟡 Medium | [1955_workflow_1955.json](workflows/1955_workflow_1955.json) |
| 1956_workflow_1956 | automate | gmail, n8n-nodes-langchain.chainsummarization, n8n-nodes-langchain.wikipedia | 🔴 High | [1956_workflow_1956.json](workflows/1956_workflow_1956.json) |
| 1957_workflow_1957 | automate | n8n-nodes-langchain.outputparserautofixing, n8n-nodes-langchain.chainllm, n8n-nodes-langchain.outputparserstructured | 🟡 Medium | [1957_workflow_1957.json](workflows/1957_workflow_1957.json) |
| 1958_workflow_1958 | automate | n8n-nodes-langchain.chainretrievalqa, n8n-nodes-langchain.lmchatopenai, manual | 🟡 Medium | [1958_workflow_1958.json](workflows/1958_workflow_1958.json) |
| 1959_workflow_1959 | automate | n8n-nodes-langchain.memorybufferwindow, n8n-nodes-langchain.chat, n8n-nodes-langchain.wikipedia | 🟡 Medium | [1959_workflow_1959.json](workflows/1959_workflow_1959.json) |
| 1960_workflow_1960 | automate | n8n-nodes-langchain.chat, n8n-nodes-langchain.embeddingsopenai, n8n-nodes-langchain.lmchatopenai | 🔴 High | [1960_workflow_1960.json](workflows/1960_workflow_1960.json) |
| 1961_workflow_1961 | automate | n8n-nodes-langchain.memorybufferwindow, slack, n8n-nodes-langchain.wikipedia | 🔴 High | [1961_workflow_1961.json](workflows/1961_workflow_1961.json) |
| 1962_workflow_1962 | automate | n8n-nodes-langchain.textsplittertokensplitter, n8n-nodes-langchain.chainsummarization, n8n-nodes-langchain.lmchatopenai | 🟡 Medium | [1962_workflow_1962.json](workflows/1962_workflow_1962.json) |
| 1963_workflow_1963 | automate | n8n-nodes-langchain.chat, n8n-nodes-langchain.lmchatopenai, manual | 🟡 Medium | [1963_workflow_1963.json](workflows/1963_workflow_1963.json) |
| 1978_workflow_1978 | automate | emailsend, httprequest, stopanderror | 🔴 High | [1978_workflow_1978.json](workflows/1978_workflow_1978.json) |
| 1980_workflow_1980 | automate | n8n-nodes-langchain.chat, n8n-nodes-langchain.chainllm, n8n-nodes-langchain.lmopenhuggingfaceinference | 🟢 Low | [1980_workflow_1980.json](workflows/1980_workflow_1980.json) |
| 1996_workflow_1996 | automate | openai, googlesheets, form | 🟡 Medium | [1996_workflow_1996.json](workflows/1996_workflow_1996.json) |
| 2006_workflow_2006 | automate | n8n-nodes-langchain.chat, httprequest, markdown | 🔴 High | [2006_workflow_2006.json](workflows/2006_workflow_2006.json) |
| 2025_workflow_2025 | automate | n8n-nodes-langchain.memorybufferwindow, n8n-nodes-langchain.chat, n8n-nodes-langchain.code | 🔴 High | [2025_workflow_2025.json](workflows/2025_workflow_2025.json) |
| 2026_workflow_2026 | automate | n8n-nodes-langchain.chat, executeworkflow, n8n-nodes-langchain.lmchatopenai | 🔴 High | [2026_workflow_2026.json](workflows/2026_workflow_2026.json) |
| 2039_workflow_2039 | automate | pipedrive, gmail, openai | 🟡 Medium | [2039_workflow_2039.json](workflows/2039_workflow_2039.json) |
| 2082_workflow_2082 | automate | n8n-nodes-langchain.code, n8n-nodes-langchain.lmchatopenai, manual | 🟡 Medium | [2082_workflow_2082.json](workflows/2082_workflow_2082.json) |
| 2083_workflow_2083 | automate | n8n-nodes-langchain.chainllm, httprequest, n8n-nodes-langchain.lmchatopenai | 🟡 Medium | [2083_workflow_2083.json](workflows/2083_workflow_2083.json) |
| 2085_workflow_2085 | automate | n8n-nodes-langchain.memorybufferwindow, n8n-nodes-langchain.chat, n8n-nodes-langchain.lmchatopenai | 🔴 High | [2085_workflow_2085.json](workflows/2085_workflow_2085.json) |
| 2090_workflow_2090 | automate | n8n-nodes-langchain.memorybufferwindow, n8n-nodes-langchain.chat, postgres | 🟡 Medium | [2090_workflow_2090.json](workflows/2090_workflow_2090.json) |
| 2094_workflow_2094 | automate | n8n-nodes-langchain.memorybufferwindow, n8n-nodes-langchain.chat, httprequest | 🔴 High | [2094_workflow_2094.json](workflows/2094_workflow_2094.json) |
| 2095_workflow_2095 | automate | n8n-nodes-langchain.memorybufferwindow, slack, n8n-nodes-langchain.chat | 🔴 High | [2095_workflow_2095.json](workflows/2095_workflow_2095.json) |
| 2098_workflow_2098 | automate | n8n-nodes-langchain.memorybufferwindow, n8n-nodes-langchain.calculator, n8n-nodes-langchain.chat | 🟡 Medium | [2098_workflow_2098.json](workflows/2098_workflow_2098.json) |
| 2114_workflow_2114 | automate | n8n-nodes-langchain.lmchatopenai, telegram, telegram | 🟢 Low | [2114_workflow_2114.json](workflows/2114_workflow_2114.json) |
| 2125_workflow_2125 | automate | gmail, httprequest, schedule | 🔴 High | [2125_workflow_2125.json](workflows/2125_workflow_2125.json) |
| 2138_workflow_2138 | automate | splitinbatches, respondtowebhook, httprequest | 🔴 High | [2138_workflow_2138.json](workflows/2138_workflow_2138.json) |
| 2139_workflow_2139 | automate | schedule, manual, n8n-nodes-langchain.openai | 🟡 Medium | [2139_workflow_2139.json](workflows/2139_workflow_2139.json) |
| 2154_workflow_2154 | automate | linear, slack, httprequest | 🔴 High | [2154_workflow_2154.json](workflows/2154_workflow_2154.json) |
| 2161_workflow_2161 | automate | n8n-nodes-langchain.memorybufferwindow, dhl, woocommerce | 🔴 High | [2161_workflow_2161.json](workflows/2161_workflow_2161.json) |
| 2165_workflow_2165 | automate | n8n-nodes-langchain.chat, n8n-nodes-langchain.embeddingsopenai, n8n-nodes-langchain.lmchatopenai | 🔴 High | [2165_workflow_2165.json](workflows/2165_workflow_2165.json) |
| 2167_workflow_2167 | automate | n8n-nodes-langchain.chainllm, httprequest, webhook | 🔴 High | [2167_workflow_2167.json](workflows/2167_workflow_2167.json) |
| 2170_workflow_2170 | automate | n8n-nodes-langchain.outputparserautofixing, n8n-nodes-langchain.chainllm, n8n-nodes-langchain.outputparserstructured | 🔴 High | [2170_workflow_2170.json](workflows/2170_workflow_2170.json) |
| 2173_workflow_2173 | automate | form, openai, respondtowebhook | 🟢 Low | [2173_workflow_2173.json](workflows/2173_workflow_2173.json) |
| 2183_workflow_2183 | automate | n8n-nodes-langchain.chainretrievalqa, n8n-nodes-langchain.chat, n8n-nodes-langchain.embeddingsopenai | 🔴 High | [2183_workflow_2183.json](workflows/2183_workflow_2183.json) |
| 2187_workflow_2187 | automate | wordpress, httprequest, n8n-nodes-langchain.wikipedia | 🔴 High | [2187_workflow_2187.json](workflows/2187_workflow_2187.json) |
| 2197_workflow_2197 | automate | n8n-nodes-langchain.chainllm, n8n-nodes-langchain.outputparserstructured, gmail | 🔴 High | [2197_workflow_2197.json](workflows/2197_workflow_2197.json) |
| 2198_workflow_2198 | automate | splitinbatches, gmail, httprequest | 🔴 High | [2198_workflow_2198.json](workflows/2198_workflow_2198.json) |
| 2216_workflow_2216 | automate | telegram, telegram, n8n-nodes-langchain.openai | 🟡 Medium | [2216_workflow_2216.json](workflows/2216_workflow_2216.json) |
| 2219_workflow_2219 | automate | gmail, gmail, n8n-nodes-langchain.chainsummarization | 🔴 High | [2219_workflow_2219.json](workflows/2219_workflow_2219.json) |
| 2233_workflow_2233 | automate | n8n-nodes-langchain.chainsummarization, schedule, n8n-nodes-langchain.lmchatopenai | 🔴 High | [2233_workflow_2233.json](workflows/2233_workflow_2233.json) |
| 2234_workflow_2234 | automate | n8n-nodes-langchain.chainsummarization, schedule, n8n-nodes-langchain.lmchatopenai | 🔴 High | [2234_workflow_2234.json](workflows/2234_workflow_2234.json) |
| 2235_workflow_2235 | automate | telegram, telegram, n8n-nodes-langchain.openai | 🟡 Medium | [2235_workflow_2235.json](workflows/2235_workflow_2235.json) |
| 2287_workflow_2287 | automate | slack, n8n-nodes-langchain.chainllm, lemlist | 🔴 High | [2287_workflow_2287.json](workflows/2287_workflow_2287.json) |
| 2315_workflow_2315 | automate | supabase, removeduplicates, n8n-nodes-langchain.outputparserstructured | 🔴 High | [2315_workflow_2315.json](workflows/2315_workflow_2315.json) |
| 2320_workflow_2320 | automate | n8n-nodes-langchain.chainllm, n8n-nodes-langchain.outputparserstructured, gmail | 🔴 High | [2320_workflow_2320.json](workflows/2320_workflow_2320.json) |
| 2321_workflow_2321 | automate | splitinbatches, slack, n8n-nodes-langchain.chainllm | 🔴 High | [2321_workflow_2321.json](workflows/2321_workflow_2321.json) |
| 2322_workflow_2322 | automate | httprequest, bannerbear, n8n-nodes-langchain.openai | 🔴 High | [2322_workflow_2322.json](workflows/2322_workflow_2322.json) |
| 2323_workflow_2323 | automate | slack, n8n-nodes-langchain.chainllm, n8n-nodes-langchain.outputparserstructured | 🔴 High | [2323_workflow_2323.json](workflows/2323_workflow_2323.json) |
| 2324_workflow_2324 | automate | splitinbatches, n8n-nodes-langchain.outputparserstructured, schedule | 🔴 High | [2324_workflow_2324.json](workflows/2324_workflow_2324.json) |
| 2326_workflow_2326 | automate | slack, n8n-nodes-langchain.outputparserstructured, n8n-nodes-langchain.serpapi | 🔴 High | [2326_workflow_2326.json](workflows/2326_workflow_2326.json) |
| 2328_workflow_2328 | automate | n8n-nodes-langchain.outputparserstructured, httprequest, googlecalendar | 🔴 High | [2328_workflow_2328.json](workflows/2328_workflow_2328.json) |
| 2330_workflow_2330 | automate | n8n-nodes-langchain.outputparserstructured, httprequest, n8n-nodes-langchain.lmchatopenai | 🔴 High | [2330_workflow_2330.json](workflows/2330_workflow_2330.json) |
| 2338_workflow_2338 | automate | n8n-nodes-langchain.outputparserstructured, readwritefile, n8n-nodes-langchain.code | 🔴 High | [2338_workflow_2338.json](workflows/2338_workflow_2338.json) |
| 2341_workflow_2341 | automate | httprequest, extractfromfile, n8n-nodes-langchain.embeddingsmistralcloud | 🔴 High | [2341_workflow_2341.json](workflows/2341_workflow_2341.json) |
| 2342_workflow_2342 | automate | n8n-nodes-langchain.outputparserautofixing, n8n-nodes-langchain.chainllm, n8n-nodes-langchain.outputparserstructured | 🔴 High | [2342_workflow_2342.json](workflows/2342_workflow_2342.json) |
| 2343_workflow_2343 | automate | n8n-nodes-langchain.httprequest, n8n-nodes-langchain.lmchatopenai, manual | 🟡 Medium | [2343_workflow_2343.json](workflows/2343_workflow_2343.json) |
| 2344_workflow_2344 | automate | n8n-nodes-langchain.vectorstoreinmemory, n8n-nodes-langchain.embeddingsopenai, manual | 🔴 High | [2344_workflow_2344.json](workflows/2344_workflow_2344.json) |
| 2346_workflow_2346 | automate | n8n-nodes-langchain.memorybufferwindow, n8n-nodes-langchain.memorymanager, n8n-nodes-langchain.lmchatopenai | 🔴 High | [2346_workflow_2346.json](workflows/2346_workflow_2346.json) |
| 2347_workflow_2347 | automate | n8n-nodes-langchain.memorybufferwindow, n8n-nodes-langchain.chat, n8n-nodes-langchain.code | 🔴 High | [2347_workflow_2347.json](workflows/2347_workflow_2347.json) |
| 2354_workflow_2354 | automate | splitinbatches, n8n-nodes-langchain.outputparserstructured, httprequest | 🔴 High | [2354_workflow_2354.json](workflows/2354_workflow_2354.json) |
| 2358_workflow_2358 | automate | n8n-nodes-langchain.chainretrievalqa, httprequest, n8n-nodes-langchain.lmchatanthropic | 🔴 High | [2358_workflow_2358.json](workflows/2358_workflow_2358.json) |
| 2370_workflow_2370 | automate | n8n-nodes-langchain.memorybufferwindow, slack, webhook | 🟡 Medium | [2370_workflow_2370.json](workflows/2370_workflow_2370.json) |
| 2372_workflow_2372 | automate | splitinbatches, executeworkflow, httprequest | 🔴 High | [2372_workflow_2372.json](workflows/2372_workflow_2372.json) |
| 2373_workflow_2373 | automate | executeworkflow, httprequest, n8n-nodes-langchain.embeddingsopenai | 🔴 High | [2373_workflow_2373.json](workflows/2373_workflow_2373.json) |
| 2374_workflow_2374 | automate | executeworkflow, httprequest, n8n-nodes-langchain.embeddingsopenai | 🔴 High | [2374_workflow_2374.json](workflows/2374_workflow_2374.json) |
| 2394_workflow_2394 | automate | schedule, todoist, n8n-nodes-langchain.openai | 🟡 Medium | [2394_workflow_2394.json](workflows/2394_workflow_2394.json) |
| 2395_workflow_2395 | automate | n8n-nodes-langchain.chainretrievalqa, supabase, n8n-nodes-langchain.vectorstoresupabase | 🔴 High | [2395_workflow_2395.json](workflows/2395_workflow_2395.json) |
| 2397_workflow_2397 | automate | n8n-nodes-langchain.memorybufferwindow, slack, webhook | 🔴 High | [2397_workflow_2397.json](workflows/2397_workflow_2397.json) |
| 2413_workflow_2413 | automate | n8n-nodes-langchain.memorybufferwindow, n8n-nodes-langchain.chat, notion | 🟡 Medium | [2413_workflow_2413.json](workflows/2413_workflow_2413.json) |
| 2415_workflow_2415 | automate | n8n-nodes-langchain.outputparserautofixing, n8n-nodes-langchain.outputparserstructured, n8n-nodes-langchain.chat | 🔴 High | [2415_workflow_2415.json](workflows/2415_workflow_2415.json) |
| 2416_workflow_2416 | automate | n8n-nodes-langchain.chainllm, n8n-nodes-langchain.outputparserstructured, httprequest | 🔴 High | [2416_workflow_2416.json](workflows/2416_workflow_2416.json) |
| 2418_workflow_2418 | automate | n8n-nodes-langchain.chainllm, n8n-nodes-langchain.outputparserstructured, httprequest | 🔴 High | [2418_workflow_2418.json](workflows/2418_workflow_2418.json) |
| 2419_workflow_2419 | automate | splitinbatches, n8n-nodes-langchain.chainllm, n8n-nodes-langchain.outputparserstructured | 🔴 High | [2419_workflow_2419.json](workflows/2419_workflow_2419.json) |
| 2420_workflow_2420 | automate | n8n-nodes-langchain.chainllm, n8n-nodes-langchain.outputparserstructured, manual | 🟡 Medium | [2420_workflow_2420.json](workflows/2420_workflow_2420.json) |
| 2421_workflow_2421 | automate | n8n-nodes-langchain.chainllm, httprequest, sort | 🔴 High | [2421_workflow_2421.json](workflows/2421_workflow_2421.json) |
| 2422_workflow_2422 | automate | venafitlsprotectcloud, slack, httprequest | 🔴 High | [2422_workflow_2422.json](workflows/2422_workflow_2422.json) |
| 2433_workflow_2433 | automate | gmail, httprequest, schedule | 🔴 High | [2433_workflow_2433.json](workflows/2433_workflow_2433.json) |
| 2434_workflow_2434 | automate | splitinbatches, strapi, wordpress | 🔴 High | [2434_workflow_2434.json](workflows/2434_workflow_2434.json) |
| 2436_workflow_2436 | automate | webhook, n8n-nodes-langchain.lmchatopenai, n8n-nodes-langchain.agent | 🟡 Medium | [2436_workflow_2436.json](workflows/2436_workflow_2436.json) |
| 2441_workflow_2441 | automate | httprequest, n8n-nodes-langchain.openai, emailreadimap | 🟡 Medium | [2441_workflow_2441.json](workflows/2441_workflow_2441.json) |
| 2446_workflow_2446 | automate | n8n-nodes-langchain.memorybufferwindow, n8n-nodes-langchain.chat, n8n-nodes-langchain.httprequest | 🔴 High | [2446_workflow_2446.json](workflows/2446_workflow_2446.json) |
| 2454_workflow_2454 | automate | splitinbatches, microsoftoutlook, markdown | 🔴 High | [2454_workflow_2454.json](workflows/2454_workflow_2454.json) |
| 2456_workflow_2456 | automate | webhook, n8n-nodes-langchain.openai, respondtowebhook | 🟡 Medium | [2456_workflow_2456.json](workflows/2456_workflow_2456.json) |
| 2462_workflow_2462 | automate | n8n-nodes-langchain.memorybufferwindow, baserow, googlecalendar | 🔴 High | [2462_workflow_2462.json](workflows/2462_workflow_2462.json) |
| 2464_workflow_2464 | automate | httprequest, sort, n8n-nodes-langchain.informationextractor | 🔴 High | [2464_workflow_2464.json](workflows/2464_workflow_2464.json) |
| 2465_workflow_2465 | automate | n8n-nodes-langchain.memorybufferwindow, n8n-nodes-langchain.vectorstore, whatsapp | 🔴 High | [2465_workflow_2465.json](workflows/2465_workflow_2465.json) |
| 2466_workflow_2466 | automate | n8n-nodes-langchain.memorybufferwindow, whatsapp, n8n-nodes-langchain.chainllm | 🔴 High | [2466_workflow_2466.json](workflows/2466_workflow_2466.json) |
| 2467_workflow_2467 | automate | splitinbatches, n8n-nodes-langchain.chainllm, httprequest | 🔴 High | [2467_workflow_2467.json](workflows/2467_workflow_2467.json) |
| 2468_workflow_2468 | automate | slack, n8n-nodes-langchain.chainllm, n8n-nodes-langchain.outputparserstructured | 🔴 High | [2468_workflow_2468.json](workflows/2468_workflow_2468.json) |
| 2473_workflow_2473 | automate | n8n-nodes-langchain.lmchatanthropic, n8n-nodes-langchain.agent, manual | 🔴 High | [2473_workflow_2473.json](workflows/2473_workflow_2473.json) |
| 2491_workflow_2491 | automate | nocodb, slack, httprequest | 🔴 High | [2491_workflow_2491.json](workflows/2491_workflow_2491.json) |
| 2502_workflow_2502 | automate | n8n-nodes-langchain.chainllm, n8n-nodes-langchain.outputparserstructured, httprequest | 🔴 High | [2502_workflow_2502.json](workflows/2502_workflow_2502.json) |
| 2513_workflow_2513 | automate | httprequest, n8n-nodes-langchain.openai | 🟡 Medium | [2513_workflow_2513.json](workflows/2513_workflow_2513.json) |
| 2525_workflow_2525 | automate | sort, googledrive, googlesheets | 🔴 High | [2525_workflow_2525.json](workflows/2525_workflow_2525.json) |
| 2552_workflow_2552 | automate | httprequest, n8n-nodes-langchain.lmchatopenai, n8n-nodes-langchain.informationextractor | 🟡 Medium | [2552_workflow_2552.json](workflows/2552_workflow_2552.json) |
| 2559_workflow_2559 | automate | n8n-nodes-langchain.memorybufferwindow, n8n-nodes-langchain.chat, httprequest | 🔴 High | [2559_workflow_2559.json](workflows/2559_workflow_2559.json) |
| 2560_workflow_2560 | automate | httprequest, schedule, n8n-nodes-langchain.lmchatopenai | 🟡 Medium | [2560_workflow_2560.json](workflows/2560_workflow_2560.json) |
| 2579_workflow_2579 | automate | n8n-nodes-langchain.chainllm, n8n-nodes-langchain.outputparserstructured, n8n-nodes-langchain.textclassifier | 🔴 High | [2579_workflow_2579.json](workflows/2579_workflow_2579.json) |
| 2580_workflow_2580 | automate | n8n-nodes-langchain.chainllm, gmail, n8n-nodes-langchain.textclassifier | 🔴 High | [2580_workflow_2580.json](workflows/2580_workflow_2580.json) |
| 2582_workflow_2582 | automate | n8n-nodes-langchain.chainllm, gmail, httprequest | 🔴 High | [2582_workflow_2582.json](workflows/2582_workflow_2582.json) |
| 2612_workflow_2612 | automate | n8n-nodes-langchain.chat, postgres, n8n-nodes-langchain.lmchatopenai | 🟡 Medium | [2612_workflow_2612.json](workflows/2612_workflow_2612.json) |
| 2618_workflow_2618 | automate | n8n-nodes-langchain.memorybufferwindow, executiondata, n8n-nodes-langchain.lmchatgroq | 🔴 High | [2618_workflow_2618.json](workflows/2618_workflow_2618.json) |
| 2619_workflow_2619 | automate | gmail, httprequest, html | 🔴 High | [2619_workflow_2619.json](workflows/2619_workflow_2619.json) |
| 2647_workflow_2647 | automate | splitinbatches, removeduplicates, slack | 🔴 High | [2647_workflow_2647.json](workflows/2647_workflow_2647.json) |
| 2648_workflow_2648 | automate | wordpress, n8n-nodes-langchain.chainllm, httprequest | 🔴 High | [2648_workflow_2648.json](workflows/2648_workflow_2648.json) |
| 2651_workflow_2651 | automate | postgres, supabase, postgres | 🔴 High | [2651_workflow_2651.json](workflows/2651_workflow_2651.json) |
| 2658_workflow_2658 | automate | httprequest, n8n-nodes-langchain.informationextractor, googledrive | 🔴 High | [2658_workflow_2658.json](workflows/2658_workflow_2658.json) |
| 2665_workflow_2665 | automate | gmail, httprequest, jira | 🔴 High | [2665_workflow_2665.json](workflows/2665_workflow_2665.json) |
| 2666_workflow_2666 | automate | gmail, httprequest, jira | 🔴 High | [2666_workflow_2666.json](workflows/2666_workflow_2666.json) |
| 2667_workflow_2667 | automate | n8n-nodes-langchain.chainretrievalqa, n8n-nodes-langchain.vectorstoreinmemory, httprequest | 🔴 High | [2667_workflow_2667.json](workflows/2667_workflow_2667.json) |
| 2679_workflow_2679 | automate | n8n-nodes-langchain.chainllm, youtube, webhook | 🔴 High | [2679_workflow_2679.json](workflows/2679_workflow_2679.json) |
| 2683_workflow_2683 | automate | httprequest, googlecalendar, webhook | 🔴 High | [2683_workflow_2683.json](workflows/2683_workflow_2683.json) |
| 2688_workflow_2688 | automate | n8n-nodes-langchain.chainllm, httprequest, schedule | 🔴 High | [2688_workflow_2688.json](workflows/2688_workflow_2688.json) |
| 2697_workflow_2697 | automate | n8n-nodes-langchain.chainllm, emailsend, httprequest | 🟡 Medium | [2697_workflow_2697.json](workflows/2697_workflow_2697.json) |
| 2700_workflow_2700 | automate | n8n-nodes-langchain.memorybufferwindow, n8n-nodes-langchain.chat, httprequest | 🔴 High | [2700_workflow_2700.json](workflows/2700_workflow_2700.json) |
| 2736_workflow_2736 | automate | n8n-nodes-langchain.chainsummarization, httprequest, n8n-nodes-langchain.lmchatopenai | 🟡 Medium | [2736_workflow_2736.json](workflows/2736_workflow_2736.json) |
| 2740_workflow_2740 | automate | n8n-nodes-langchain.memorybufferwindow, gmail, n8n-nodes-langchain.lmchatopenai | 🟡 Medium | [2740_workflow_2740.json](workflows/2740_workflow_2740.json) |
| 2749_workflow_2749 | automate | n8n-nodes-langchain.outputparserautofixing, n8n-nodes-langchain.outputparserstructured, gmail | 🔴 High | [2749_workflow_2749.json](workflows/2749_workflow_2749.json) |
| 2757_workflow_2757 | automate | httprequest, microsoftoutlook, erpnext | 🔴 High | [2757_workflow_2757.json](workflows/2757_workflow_2757.json) |
| 2758_workflow_2758 | automate | googlesheets, httprequest, microsoftoutlook | 🔴 High | [2758_workflow_2758.json](workflows/2758_workflow_2758.json) |
| 2771_workflow_2771 | automate | splitinbatches, n8n-nodes-langchain.chainllm, httprequest | 🔴 High | [2771_workflow_2771.json](workflows/2771_workflow_2771.json) |
| 2779_workflow_2779 | automate | extractfromfile, googledrive, n8n-nodes-langchain.openai | 🟡 Medium | [2779_workflow_2779.json](workflows/2779_workflow_2779.json) |
| 2780_workflow_2780 | automate | splitinbatches, n8n-nodes-langchain.chainllm, httprequest | 🔴 High | [2780_workflow_2780.json](workflows/2780_workflow_2780.json) |
| 2786_workflow_2786 | automate | n8n-nodes-langchain.memorybufferwindow, n8n-nodes-langchain.chat, httprequest | 🔴 High | [2786_workflow_2786.json](workflows/2786_workflow_2786.json) |
| 2790_workflow_2790 | automate | gmail, emailsend, n8n-nodes-langchain.lmchatgooglegemini | 🔴 High | [2790_workflow_2790.json](workflows/2790_workflow_2790.json) |
| 2823_workflow_2823 | automate | n8n-nodes-langchain.chainllm, n8n-nodes-langchain.outputparserstructured, emailsend | 🔴 High | [2823_workflow_2823.json](workflows/2823_workflow_2823.json) |
| 2840_workflow_2840 | automate | n8n-nodes-langchain.memorybufferwindow, splitinbatches, n8n-nodes-langchain.textsplittertokensplitter | 🔴 High | [2840_workflow_2840.json](workflows/2840_workflow_2840.json) |
| 2878_workflow_2878 | automate | n8n-nodes-langchain.outputparserstructured, httprequest, splitinbatches | 🔴 High | [2878_workflow_2878.json](workflows/2878_workflow_2878.json) |
| 2922_workflow_2922 | automate | n8n-nodes-langchain.lmollama, n8n-nodes-langchain.chainllm, manual | 🔴 High | [2922_workflow_2922.json](workflows/2922_workflow_2922.json) |
| 2931_workflow_2931 | automate | n8n-nodes-langchain.memorybufferwindow, n8n-nodes-langchain.wikipedia, n8n-nodes-langchain.httprequest | 🟡 Medium | [2931_workflow_2931.json](workflows/2931_workflow_2931.json) |
| 2945_workflow_2945 | automate | splitinbatches, n8n-nodes-langchain.outputparserstructured, n8n-nodes-langchain.lmchatopenai | 🟡 Medium | [2945_workflow_2945.json](workflows/2945_workflow_2945.json) |
| 2972_workflow_2972 | automate | n8n-nodes-langchain.chainllm, n8n-nodes-langchain.outputparserstructured, n8n-nodes-langchain.textclassifier | 🔴 High | [2972_workflow_2972.json](workflows/2972_workflow_2972.json) |
| 2976_workflow_2976 | automate | n8n-nodes-langchain.outputparserstructured, youtube, googledocs | 🟡 Medium | [2976_workflow_2976.json](workflows/2976_workflow_2976.json) |
| 3020_workflow_3020 | automate | n8n-nodes-langchain.chat, n8n-nodes-langchain.httprequest, n8n-nodes-langchain.lmchatopenai | 🟡 Medium | [3020_workflow_3020.json](workflows/3020_workflow_3020.json) |
| 3027_workflow_3027 | automate | n8n-nodes-langchain.outputparserautofixing, n8n-nodes-langchain.chainllm, n8n-nodes-langchain.outputparserstructured | 🟡 Medium | [3027_workflow_3027.json](workflows/3027_workflow_3027.json) |
| 3028_workflow_3028 | automate | wordpress, n8n-nodes-langchain.chainllm, httprequest | 🟡 Medium | [3028_workflow_3028.json](workflows/3028_workflow_3028.json) |
| 3035_workflow_3035 | automate | n8n-nodes-langchain.lmchatazureopenai, n8n-nodes-langchain.outputparserstructured, n8n-nodes-langchain.agent | 🔴 High | [3035_workflow_3035.json](workflows/3035_workflow_3035.json) |
| 3042_workflow_3042 | automate | slack, schedule, webhook | 🔴 High | [3042_workflow_3042.json](workflows/3042_workflow_3042.json) |
| 3050_workflow_3050 | automate | n8n-nodes-langchain.memorybufferwindow, n8n-nodes-langchain.calculator, googlesheets | 🔴 High | [3050_workflow_3050.json](workflows/3050_workflow_3050.json) |
| 3052_workflow_3052 | automate | n8n-nodes-langchain.chainllm, n8n-nodes-langchain.outputparserstructured, telegram | 🔴 High | [3052_workflow_3052.json](workflows/3052_workflow_3052.json) |
| 3053_workflow_3053 | automate | n8n-nodes-langchain.memorybufferwindow, airtable, splitinbatches | 🔴 High | [3053_workflow_3053.json](workflows/3053_workflow_3053.json) |
| 3057_workflow_3057 | automate | n8n-nodes-langchain.serpapi, n8n-nodes-langchain.outputparserstructured, httprequest | 🔴 High | [3057_workflow_3057.json](workflows/3057_workflow_3057.json) |
| 3078_workflow_3078 | automate | splitinbatches, httprequest, n8n-nodes-langchain.lmchatgooglegemini | 🔴 High | [3078_workflow_3078.json](workflows/3078_workflow_3078.json) |
| 3107_workflow_3107 | automate | n8n-nodes-langchain.outputparserautofixing, n8n-nodes-langchain.chainllm, n8n-nodes-langchain.outputparserstructured | 🔴 High | [3107_workflow_3107.json](workflows/3107_workflow_3107.json) |
| 3115_workflow_3115 | automate | executiondata, n8n-nodes-langchain.textclassifier, httprequest | 🔴 High | [3115_workflow_3115.json](workflows/3115_workflow_3115.json) |
| 3123_workflow_3123 | automate | splitinbatches, n8n-nodes-langchain.outputparserstructured, gmail | 🔴 High | [3123_workflow_3123.json](workflows/3123_workflow_3123.json) |
| 3161_workflow_3161 | automate | googlesheets, twitter, openai | 🟢 Low | [3161_workflow_3161.json](workflows/3161_workflow_3161.json) |
| 3194_workflow_3194 | automate | n8n-nodes-langchain.chainllm, n8n-nodes-langchain.outputparserstructured, gmail | 🔴 High | [3194_workflow_3194.json](workflows/3194_workflow_3194.json) |
| 3195_workflow_3195 | automate | n8n-nodes-langchain.outputparserstructured, httprequest, googlesheets | 🔴 High | [3195_workflow_3195.json](workflows/3195_workflow_3195.json) |
| 3277_workflow_3277 | automate | gmail, gmail, n8n-nodes-langchain.textclassifier | 🔴 High | [3277_workflow_3277.json](workflows/3277_workflow_3277.json) |
| 3295_workflow_3295 | automate | n8n-nodes-langchain.memorybufferwindow, telegram, n8n-nodes-langchain.lmchatopenai | 🟡 Medium | [3295_workflow_3295.json](workflows/3295_workflow_3295.json) |
| 3303_workflow_3303 | automate | n8n-nodes-langchain.chat, n8n-nodes-langchain.lmchatopenai, n8n-nodes-langchain.agent | 🟢 Low | [3303_workflow_3303.json](workflows/3303_workflow_3303.json) |
| 3304_workflow_3304 | automate | emailsend, form, html | 🟡 Medium | [3304_workflow_3304.json](workflows/3304_workflow_3304.json) |
| 3305_workflow_3305 | automate | n8n-nodes-langchain.memorybufferwindow, n8n-nodes-langchain.chat, googlebigquery | 🔴 High | [3305_workflow_3305.json](workflows/3305_workflow_3305.json) |
| 3314_workflow_3314 | automate | gmail, httprequest, n8n-nodes-langchain.lmchatopenai | 🔴 High | [3314_workflow_3314.json](workflows/3314_workflow_3314.json) |
| 3344_workflow_3344 | automate | n8n-nodes-langchain.outputparserstructured, gmail, n8n-nodes-langchain.lmchatopenai | 🟡 Medium | [3344_workflow_3344.json](workflows/3344_workflow_3344.json) |
| 3350_workflow_3350 | automate | redis, n8n-nodes-langchain.memoryredischat, n8n-nodes-langchain.lmchatopenai | 🔴 High | [3350_workflow_3350.json](workflows/3350_workflow_3350.json) |
| 3351_workflow_3351 | automate | splitinbatches, n8n-nodes-langchain.textclassifier, executeworkflow | 🔴 High | [3351_workflow_3351.json](workflows/3351_workflow_3351.json) |
| 3395_workflow_3395 | automate | splitinbatches, n8n-nodes-langchain.vectorstoresupabase, schedule | 🔴 High | [3395_workflow_3395.json](workflows/3395_workflow_3395.json) |
| 3396_workflow_3396 | automate | splitinbatches, n8n-nodes-langchain.textclassifier, microsoftoutlook | 🔴 High | [3396_workflow_3396.json](workflows/3396_workflow_3396.json) |
| 3397_workflow_3397 | automate | splitinbatches, hubspot, gmail | 🔴 High | [3397_workflow_3397.json](workflows/3397_workflow_3397.json) |
| 3420_workflow_3420 | automate | n8n-nodes-langchain.outputparserstructured, gmail, gmail | 🔴 High | [3420_workflow_3420.json](workflows/3420_workflow_3420.json) |
| 3446_workflow_3446 | automate | splitinbatches, n8n-nodes-langchain.chainllm, httprequest | 🔴 High | [3446_workflow_3446.json](workflows/3446_workflow_3446.json) |
| 3449_workflow_3449 | automate | n8n-nodes-langchain.memorybufferwindow, microsoftoutlook, slack | 🔴 High | [3449_workflow_3449.json](workflows/3449_workflow_3449.json) |
| 3478_workflow_3478 | automate | googledrive, facebookgraphapi, googlesheets | 🟡 Medium | [3478_workflow_3478.json](workflows/3478_workflow_3478.json) |
| 3498_workflow_3498 | automate | n8n-nodes-langchain.memorybufferwindow, n8n-nodes-langchain.chat, httprequest | 🔴 High | [3498_workflow_3498.json](workflows/3498_workflow_3498.json) |
| 3499_workflow_3499 | automate | n8n-nodes-langchain.memorybufferwindow, airtable, n8n-nodes-langchain.lmchatopenai | 🔴 High | [3499_workflow_3499.json](workflows/3499_workflow_3499.json) |
| 3500_workflow_3500 | automate | splitinbatches, ghost, n8n-nodes-langchain.lmchatopenai | 🔴 High | [3500_workflow_3500.json](workflows/3500_workflow_3500.json) |
| 3505_workflow_3505 | automate | gmail, httprequest, sort | 🔴 High | [3505_workflow_3505.json](workflows/3505_workflow_3505.json) |
| 3509_workflow_3509 | automate | gmail, linkedin, manual | 🟡 Medium | [3509_workflow_3509.json](workflows/3509_workflow_3509.json) |
| 3517_workflow_3517 | automate | splitinbatches, n8n-nodes-langchain.lmchatopenai, manual | 🔴 High | [3517_workflow_3517.json](workflows/3517_workflow_3517.json) |
| 3545_workflow_3545 | automate | n8n-nodes-langchain.textclassifier, microsoftoutlook, n8n-nodes-langchain.lmchatopenai | 🔴 High | [3545_workflow_3545.json](workflows/3545_workflow_3545.json) |
| 3546_workflow_3546 | automate | n8n-nodes-langchain.outputparserstructured, gmail, n8n-nodes-langchain.lmchatopenai | 🟡 Medium | [3546_workflow_3546.json](workflows/3546_workflow_3546.json) |
| 3561_workflow_3561 | automate | splitinbatches, n8n-nodes-langchain.chainllm, httprequest | 🔴 High | [3561_workflow_3561.json](workflows/3561_workflow_3561.json) |
| 3564_workflow_3564 | automate | emailsend, httprequest, rssfeedread | 🔴 High | [3564_workflow_3564.json](workflows/3564_workflow_3564.json) |
| 3574_workflow_3574 | automate | n8n-nodes-langchain.chainretrievalqa, n8n-nodes-langchain.chat, httprequest | 🔴 High | [3574_workflow_3574.json](workflows/3574_workflow_3574.json) |
| 3599_workflow_3599 | automate | googlesheets, n8n-nodes-langchain.outputparserstructured, n8n-nodes-langchain.chat | 🔴 High | [3599_workflow_3599.json](workflows/3599_workflow_3599.json) |
| 3601_workflow_3601 | automate | n8n-nodes-langchain.chainllm, httprequest, n8n-nodes-langchain.lmchatopenai | 🔴 High | [3601_workflow_3601.json](workflows/3601_workflow_3601.json) |
| 3607_workflow_3607 | automate | n8n-nodes-langchain.chainllm, httprequest, n8n-nodes-langchain.lmchatopenai | 🔴 High | [3607_workflow_3607.json](workflows/3607_workflow_3607.json) |
| 3610_workflow_3610 | automate | n8n-nodes-langchain.chainllm, gmail, httprequest | 🔴 High | [3610_workflow_3610.json](workflows/3610_workflow_3610.json) |
| 3617_workflow_3617 | automate | splitinbatches, n8n-nodes-langchain.calculator, datetime | 🔴 High | [3617_workflow_3617.json](workflows/3617_workflow_3617.json) |
| 3624_workflow_3624 | automate | n8n-nodes-langchain.chainllm, gmail, httprequest | 🔴 High | [3624_workflow_3624.json](workflows/3624_workflow_3624.json) |
| 3634_workflow_3634 | automate | n8n-nodes-langchain.mcp, n8n-nodes-langchain.workflow, googledrive | 🔴 High | [3634_workflow_3634.json](workflows/3634_workflow_3634.json) |
| 3636_workflow_3636 | automate | httprequest, n8n-nodes-langchain.mcp, n8n-nodes-langchain.embeddingsopenai | 🔴 High | [3636_workflow_3636.json](workflows/3636_workflow_3636.json) |
| 3640_workflow_3640 | automate | splitinbatches, httprequest, manual | 🔴 High | [3640_workflow_3640.json](workflows/3640_workflow_3640.json) |
| 3644_workflow_3644 | automate | splitinbatches, googletasks, httprequest | 🔴 High | [3644_workflow_3644.json](workflows/3644_workflow_3644.json) |
| 3656_workflow_3656 | automate | n8n-nodes-langchain.memorybufferwindow, googletasks, n8n-nodes-langchain.mcp | 🔴 High | [3656_workflow_3656.json](workflows/3656_workflow_3656.json) |
| 3684_workflow_3684 | automate | splitinbatches, n8n-nodes-langchain.outputparserstructured, gmail | 🔴 High | [3684_workflow_3684.json](workflows/3684_workflow_3684.json) |
| 3700_workflow_3700 | automate | n8n-nodes-langchain.chainllm, httprequest, n8n-nodes-langchain.lmchatopenai | 🔴 High | [3700_workflow_3700.json](workflows/3700_workflow_3700.json) |
| 3706_workflow_3706 | automate | hubspot, n8n-nodes-langchain.chainsummarization, form | 🔴 High | [3706_workflow_3706.json](workflows/3706_workflow_3706.json) |
| 3719_workflow_3719 | automate | gmail, webhook, googledrive | 🔴 High | [3719_workflow_3719.json](workflows/3719_workflow_3719.json) |
| 3767_workflow_3767 | automate | hubspot, n8n-nodes-langchain.chainllm, n8n-nodes-langchain.outputparserstructured | 🔴 High | [3767_workflow_3767.json](workflows/3767_workflow_3767.json) |
| 3770_workflow_3770 | automate | n8n-nodes-langchain.memorybufferwindow, redis, n8n-nodes-langchain.chat | 🔴 High | [3770_workflow_3770.json](workflows/3770_workflow_3770.json) |
| 3790_workflow_3790 | automate | n8n-nodes-langchain.memorybufferwindow, n8n-nodes-langchain.outputparserstructured, emailsend | 🔴 High | [3790_workflow_3790.json](workflows/3790_workflow_3790.json) |
| 3830_workflow_3830 | automate | splitinbatches, slack, httprequest | 🔴 High | [3830_workflow_3830.json](workflows/3830_workflow_3830.json) |
| 3832_workflow_3832 | automate | n8n-nodes-langchain.chat, executeworkflow, n8n-nodes-langchain.lmchatopenai | 🔴 High | [3832_workflow_3832.json](workflows/3832_workflow_3832.json) |
| 3840_workflow_3840 | automate | n8n-nodes-langchain.chainllm, n8n-nodes-langchain.outputparserstructured, httprequest | 🔴 High | [3840_workflow_3840.json](workflows/3840_workflow_3840.json) |
| 3868_workflow_3868 | automate | splitinbatches, n8n-nodes-langchain.chainllm, n8n-nodes-langchain.outputparserstructured | 🔴 High | [3868_workflow_3868.json](workflows/3868_workflow_3868.json) |
| 3891_workflow_3891 | automate | reddit, n8n-nodes-langchain.outputparserstructured, n8n-nodes-langchain.lmchatanthropic | 🔴 High | [3891_workflow_3891.json](workflows/3891_workflow_3891.json) |
| 3893_workflow_3893 | automate | n8n-nodes-langchain.chainllm, n8n-nodes-langchain.outputparserstructured, microsoftoutlook | 🔴 High | [3893_workflow_3893.json](workflows/3893_workflow_3893.json) |
| 3899_workflow_3899 | automate | n8n-nodes-langchain.chainllm, n8n-nodes-langchain.outputparserstructured, gmail | 🔴 High | [3899_workflow_3899.json](workflows/3899_workflow_3899.json) |
| 3930_workflow_3930 | automate | n8n-nodes-langchain.chainllm, n8n-nodes-langchain.outputparserstructured, gmail | 🔴 High | [3930_workflow_3930.json](workflows/3930_workflow_3930.json) |
| 3942_workflow_3942 | automate | splitinbatches, n8n-nodes-langchain.memorybufferwindow, n8n-nodes-langchain.chat | 🔴 High | [3942_workflow_3942.json](workflows/3942_workflow_3942.json) |
| 3958_workflow_3958 | automate | hubspot, n8n-nodes-langchain.outputparserstructured, gmail | 🔴 High | [3958_workflow_3958.json](workflows/3958_workflow_3958.json) |
| 3969_workflow_3969 | automate | splitinbatches, slack, n8n-nodes-langchain.chainllm | 🔴 High | [3969_workflow_3969.json](workflows/3969_workflow_3969.json) |
| 3971_workflow_3971 | automate | n8n-nodes-langchain.chainllm, markdown, schedule | 🔴 High | [3971_workflow_3971.json](workflows/3971_workflow_3971.json) |
| 3D Figurine Orthographic Views with Midjourney and GPT-4o-Image API | automate | httprequest, manual | 🟡 Medium | [9r4T5kELOXAV8L1F_3D_Figurine_Orthographic_Views_with_Midjourney_and_GPT-4o-Image_API.json](workflows/9r4T5kELOXAV8L1F_3D_Figurine_Orthographic_Views_with_Midjourney_and_GPT-4o-Image_API.json) |
| 4001_workflow_4001 | automate | splitinbatches, n8n-nodes-langchain.chainllm, n8n-nodes-langchain.outputparserstructured | 🔴 High | [4001_workflow_4001.json](workflows/4001_workflow_4001.json) |
| A/B Split Testing | automate | supabase, n8n-nodes-langchain.memorypostgreschat, n8n-nodes-langchain.chat | 🔴 High | [TEA7K9MSVQGCWKe6_A_B_Split_Testing.json](workflows/TEA7K9MSVQGCWKe6_A_B_Split_Testing.json) |
| Adaptive RAG | automate | n8n-nodes-langchain.memorybufferwindow, n8n-nodes-langchain.chat, n8n-nodes-langchain.embeddingsgooglegemini | 🔴 High | [cpuFyJYHKmjHTncz_Adaptive_RAG.json](workflows/cpuFyJYHKmjHTncz_Adaptive_RAG.json) |
| Agent Access Control Template | automate | n8n-nodes-langchain.memorybufferwindow, n8n-nodes-langchain.calculator, n8n-nodes-langchain.code | 🔴 High | [fa2TGWrY9rPurC30_Agent_Access_Control_Template.json](workflows/fa2TGWrY9rPurC30_Agent_Access_Control_Template.json) |
| Agent Milvus tool | automate | n8n-nodes-langchain.chat, httprequest, n8n-nodes-langchain.vectorstoremilvus | 🔴 High | [A5R7XYSzrCJKlw9k_Agent_Milvus_tool.json](workflows/A5R7XYSzrCJKlw9k_Agent_Milvus_tool.json) |
| Agent with custom HTTP Request | automate | httprequest, markdown, n8n-nodes-langchain.manualchat | 🔴 High | [AI agent that can scrape webpages.json](workflows/AI agent that can scrape webpages.json) |
| Ahrefs Keyword Research Workflow | automate | n8n-nodes-langchain.memorybufferwindow, n8n-nodes-langchain.chat, httprequest | 🔴 High | [OO4izN00xPfIPGaB_Ahrefs_Keyword_Research_Workflow.json](workflows/OO4izN00xPfIPGaB_Ahrefs_Keyword_Research_Workflow.json) |
| Ask a human | automate | n8n-nodes-langchain.memorybufferwindow, slack, n8n-nodes-langchain.chat | 🔴 High | [Ask a human for help when the AI doesn_t know the answer.json](workflows/Ask a human for help when the AI doesn_t know the answer.json) |
| Auto Knowledge Base Article Generator | automate | n8n-nodes-langchain.chat, httprequest, n8n-nodes-langchain.lmchatopenai | 🔴 High | [WwEFqNK4YP6UJcg2_Auto_Knowledge_Base_Article_Generator.json](workflows/WwEFqNK4YP6UJcg2_Auto_Knowledge_Base_Article_Generator.json) |
| Auto WordPress Blog Generator (GPT + Postgres + WP Media) | automate | postgres, httprequest, schedule | 🔴 High | [17j2efAe10uXRc4p_Auto_WordPress_Blog_Generator_(GPT_+_Postgres_+_WP_Media).json](workflows/17j2efAe10uXRc4p_Auto_WordPress_Blog_Generator_(GPT_+_Postgres_+_WP_Media).json) |
| Auto categorize wordpress template | automate | wordpress, n8n-nodes-langchain.lmchatopenai, manual | 🟡 Medium | [caaf1WFANPKAikiH_Auto_categorize_wordpress_template.json](workflows/caaf1WFANPKAikiH_Auto_categorize_wordpress_template.json) |
| Auto categorize wordpress template | automate | wordpress, n8n-nodes-langchain.lmchatopenai, manual | 🟡 Medium | [Auto-Categorize blog posts in wordpress using A.I..json](workflows/Auto-Categorize blog posts in wordpress using A.I..json) |
| Automate Content Generator for WordPress with DeepSeek R1 | automate | wordpress, httprequest, manual | 🔴 High | [p5bfwpcRy6LK33Io_Automate_Content_Generator_for_WordPress_with_DeepSeek_R1.json](workflows/p5bfwpcRy6LK33Io_Automate_Content_Generator_for_WordPress_with_DeepSeek_R1.json) |
| Automate Content Generator for WordPress with DeepSeek R1 | automate | wordpress, httprequest, manual | 🔴 High | [Automate Content Generator for WordPress with DeepSeek R1.json](workflows/Automate Content Generator for WordPress with DeepSeek R1.json) |
| Automated Content Generation & Publishing - Wordpress | automate | wordpress, httprequest, schedule | 🔴 High | [YOUR_WORKFLOW_ID_Automated_Content_Generation_&_Publishing_-_Wordpress.json](workflows/YOUR_WORKFLOW_ID_Automated_Content_Generation_&_Publishing_-_Wordpress.json) |
| Automated Image Metadata Tagging | automate | extractfromfile, googledrive, converttofile | 🟡 Medium | [XbawQw3cvClu2wsx_Automated_Image_Metadata_Tagging.json](workflows/XbawQw3cvClu2wsx_Automated_Image_Metadata_Tagging.json) |
| Automated Image Metadata Tagging (Community Node) | automate | googledrive, n8n-nodes-langchain.openai, googledrive | 🟡 Medium | [4nBQyhwqDqmXY2AL_Automated_Image_Metadata_Tagging_(Community_Node).json](workflows/4nBQyhwqDqmXY2AL_Automated_Image_Metadata_Tagging_(Community_Node).json) |
| Automated PDF to HTML Conversion | automate | httprequest, googledrive, googledrive | 🟡 Medium | [3McL3itHTso0Cy10_Automated_PDF_to_HTML_Conversion.json](workflows/3McL3itHTso0Cy10_Automated_PDF_to_HTML_Conversion.json) |
| Automatizacion X | automate | n8n-nodes-langchain.memorybufferwindow, twitter, n8n-nodes-langchain.chat | 🟡 Medium | [WCh8N9PrO0UIwrqW_Automatizacion_X.json](workflows/WCh8N9PrO0UIwrqW_Automatizacion_X.json) |
| Baserow markdown to html | automate | markdown, baserow, webhook | 🟡 Medium | [cMccNWyyvptrhRt6_Baserow_markdown_to_html.json](workflows/cMccNWyyvptrhRt6_Baserow_markdown_to_html.json) |
| Bitrix24 Open Chanel RAG Chatbot Application Workflow example with Webhook Integration | automate | n8n-nodes-langchain.chainretrievalqa, httprequest, n8n-nodes-langchain.embeddingsollama | 🔴 High | [TBiW9x7O4ijo4yOX_Bitrix24_Open_Chanel_RAG_Chatbot_Application_Workflow_example_with_Webhook_Integration.json](workflows/TBiW9x7O4ijo4yOX_Bitrix24_Open_Chanel_RAG_Chatbot_Application_Workflow_example_with_Webhook_Integration.json) |
| Blog Automation TEMPLATE | automate | n8n-nodes-langchain.chainllm, httprequest, schedule | 🔴 High | [Author and Publish Blog Posts From Google Sheets.json](workflows/Author and Publish Blog Posts From Google Sheets.json) |
| Blog Automation TEMPLATE | automate | n8n-nodes-langchain.chainllm, httprequest, schedule | 🔴 High | [b0KRVIuuUxE5afHo_Blog_Automation_TEMPLATE.json](workflows/b0KRVIuuUxE5afHo_Blog_Automation_TEMPLATE.json) |
| Build a Chatbot, Voice Agent and Phone Agent with Voiceflow, Google Calendar and RAG | automate | n8n-nodes-langchain.vectorstore, n8n-nodes-langchain.chainllm, n8n-nodes-langchain.outputparserstructured | 🔴 High | [MMDt8lGtac2oU8nI_Build_a_Chatbot,_Voice_Agent_and_Phone_Agent_with_Voiceflow,_Google_Calendar_and_RAG.json](workflows/MMDt8lGtac2oU8nI_Build_a_Chatbot,_Voice_Agent_and_Phone_Agent_with_Voiceflow,_Google_Calendar_and_RAG.json) |
| Build an MCP Server with Google Calendar | automate | n8n-nodes-langchain.memorybufferwindow, n8n-nodes-langchain.chat, googlecalendar | 🔴 High | [5opbTWPZRN05bYdz_Build_an_MCP_Server_with_Google_Calendar.json](workflows/5opbTWPZRN05bYdz_Build_an_MCP_Server_with_Google_Calendar.json) |
| Building Your First WhatsApp Chatbot | automate | n8n-nodes-langchain.memorybufferwindow, n8n-nodes-langchain.vectorstore, whatsapp | 🔴 High | [Building Your First WhatsApp Chatbot.json](workflows/Building Your First WhatsApp Chatbot.json) |
| Building Your First WhatsApp Chatbot (1) | automate | n8n-nodes-langchain.memorybufferwindow, n8n-nodes-langchain.vectorstore, whatsapp | 🔴 High | [Building Your First WhatsApp Chatbot (1).json](workflows/Building Your First WhatsApp Chatbot (1).json) |
| Business Canvas Generator | automate | n8n-nodes-langchain.chat, n8n-nodes-langchain.lmchatollama, n8n-nodes-langchain.agent | 🔴 High | [lStrENIdqN2WyGqW_Business_Canvas_Generator.json](workflows/lStrENIdqN2WyGqW_Business_Canvas_Generator.json) |
| Calendar_scheduling | automate | itemlists, n8n-nodes-langchain.chainllm, gmail | 🔴 High | [Suggest meeting slots using AI.json](workflows/Suggest meeting slots using AI.json) |
| Chat with Google Sheet | automate | n8n-nodes-langchain.chat, n8n-nodes-langchain.lmchatopenai, n8n-nodes-langchain.workflow | 🔴 High | [Chat with a Google Sheet using AI.json](workflows/Chat with a Google Sheet using AI.json) |
| Chat with Postgresql Database | automate | n8n-nodes-langchain.memorybufferwindow, n8n-nodes-langchain.chat, postgres | 🟡 Medium | [Chat with Postgresql Database.json](workflows/Chat with Postgresql Database.json) |
| Chat with Postgresql Database | automate | n8n-nodes-langchain.memorybufferwindow, n8n-nodes-langchain.chat, postgres | 🟡 Medium | [eOUewYsEzJmQixI6_Chat_with_Postgresql_Database.json](workflows/eOUewYsEzJmQixI6_Chat_with_Postgresql_Database.json) |
| Chat with local LLMs using n8n and Ollama | automate | n8n-nodes-langchain.chat, n8n-nodes-langchain.chainllm, n8n-nodes-langchain.lmchatollama | 🟢 Low | [Chat with local LLMs using n8n and Ollama.json](workflows/Chat with local LLMs using n8n and Ollama.json) |
| Chat with local LLMs using n8n and Ollama | automate | n8n-nodes-langchain.chat, n8n-nodes-langchain.chainllm, n8n-nodes-langchain.lmchatollama | 🟢 Low | [af8RV5b2TWB2LclA_Chat_with_local_LLMs_using_n8n_and_Ollama.json](workflows/af8RV5b2TWB2LclA_Chat_with_local_LLMs_using_n8n_and_Ollama.json) |
| ChatGPT Automatic Code Review in Gitlab MR | automate | n8n-nodes-langchain.chainllm, httprequest, webhook | 🔴 High | [ChatGPT Automatic Code Review in Gitlab MR.json](workflows/ChatGPT Automatic Code Review in Gitlab MR.json) |
| ClockifyBlockiaWorkflow | automate | n8n-nodes-langchain.memorybufferwindow, executiondata, n8n-nodes-langchain.calculator | 🔴 High | [WsksMHrmAQrG32db_ClockifyBlockiaWorkflow.json](workflows/WsksMHrmAQrG32db_ClockifyBlockiaWorkflow.json) |
| Code Review workflow | automate | github, googlesheets, httprequest | 🔴 High | [AMQub0Da16qevkJS_Code_Review_workflow.json](workflows/AMQub0Da16qevkJS_Code_Review_workflow.json) |
| CoinMarketCap_Crypto_Agent_Tool | automate | n8n-nodes-langchain.memorybufferwindow, n8n-nodes-langchain.httprequest, n8n-nodes-langchain.lmchatopenai | 🟡 Medium | [R4EuB1gx1IpMXCJM_CoinMarketCap_Crypto_Agent_Tool.json](workflows/R4EuB1gx1IpMXCJM_CoinMarketCap_Crypto_Agent_Tool.json) |
| CoinMarketCap_DEXScan_Agent_Tool | automate | n8n-nodes-langchain.memorybufferwindow, n8n-nodes-langchain.httprequest, n8n-nodes-langchain.lmchatopenai | 🔴 High | [ImiznkEUWCkKbg1w_CoinMarketCap_DEXScan_Agent_Tool.json](workflows/ImiznkEUWCkKbg1w_CoinMarketCap_DEXScan_Agent_Tool.json) |
| CoinMarketCap_Exchange_and_Community_Agent_Tool | automate | n8n-nodes-langchain.memorybufferwindow, n8n-nodes-langchain.httprequest, n8n-nodes-langchain.lmchatopenai | 🟡 Medium | [kbJb4VMD3SZlcS2u_CoinMarketCap_Exchange_and_Community_Agent_Tool.json](workflows/kbJb4VMD3SZlcS2u_CoinMarketCap_Exchange_and_Community_Agent_Tool.json) |
| Coinmarketcap Price Agent | automate | n8n-nodes-langchain.memorybufferwindow, n8n-nodes-langchain.httprequest, telegram | 🟡 Medium | [FQ0Uljxi7aIBdTFX_Coinmarketcap_Price_Agent.json](workflows/FQ0Uljxi7aIBdTFX_Coinmarketcap_Price_Agent.json) |
| Complete Youtube | automate | n8n-nodes-langchain.memorybufferwindow, splitinbatches, n8n-nodes-langchain.chat | 🔴 High | [AI Youtube Trend Finder Based On Niche.json](workflows/AI Youtube Trend Finder Based On Niche.json) |
| Complete Youtube | automate | n8n-nodes-langchain.memorybufferwindow, splitinbatches, n8n-nodes-langchain.chat | 🔴 High | [XSyVFC1tsGSxNwX9_Complete_Youtube.json](workflows/XSyVFC1tsGSxNwX9_Complete_Youtube.json) |
| Contact Form Text Classifier for eCommerce | automate | n8n-nodes-langchain.textclassifier, emailsend, n8n-nodes-langchain.lmchatopenai | 🟡 Medium | [Modular & Customizable AI-Powered Email Routing_ Text Classifier for eCommerce.json](workflows/Modular & Customizable AI-Powered Email Routing_ Text Classifier for eCommerce.json) |
| Contact Form Text Classifier for eCommerce | automate | n8n-nodes-langchain.textclassifier, emailsend, n8n-nodes-langchain.lmchatopenai | 🟡 Medium | [LGpVLWPpNZSt9ISM_Contact_Form_Text_Classifier_for_eCommerce.json](workflows/LGpVLWPpNZSt9ISM_Contact_Form_Text_Classifier_for_eCommerce.json) |
| Content to 9:16 Aspect Image Generator v1 | automate | splitinbatches, httprequest, n8n-nodes-langchain.wikipedia | 🔴 High | [Generate 9_16 Images from Content and Brand Guidelines.json](workflows/Generate 9_16 Images from Content and Brand Guidelines.json) |
| Customer Support Channel and Ticketing System with Slack and Linear | automate | slack, n8n-nodes-langchain.chainllm, n8n-nodes-langchain.outputparserstructured | 🔴 High | [Customer Support Channel and Ticketing System with Slack and Linear.json](workflows/Customer Support Channel and Ticketing System with Slack and Linear.json) |
| Customer and Sales Support | automate | n8n-nodes-langchain.memorybufferwindow, googlesheets, n8n-nodes-langchain.chat | 🟡 Medium | [7Pw91QNT4UGeNmL5_Customer_and_Sales_Support.json](workflows/7Pw91QNT4UGeNmL5_Customer_and_Sales_Support.json) |
| DSP Agent | automate | n8n-nodes-langchain.memorybufferwindow, airtable, n8n-nodes-langchain.calculator | 🔴 High | [DSP_Agent.json](workflows/DSP_Agent.json) |
| Discord Agent | automate | n8n-nodes-langchain.memorybufferwindow, n8n-nodes-langchain.chat, n8n-nodes-langchain.lmchatopenai | 🟡 Medium | [A4hqQNFLymCRKnYK_Discord_Agent.json](workflows/A4hqQNFLymCRKnYK_Discord_Agent.json) |
| Discord MCP Chat Agent | automate | n8n-nodes-langchain.chat, n8n-nodes-langchain.lmchatopenai, n8n-nodes-langchain.mcpclient | 🟡 Medium | [xRclXA5QzrT3c6U8_Discord_MCP_Chat_Agent.json](workflows/xRclXA5QzrT3c6U8_Discord_MCP_Chat_Agent.json) |
| Docsify example | automate | n8n-nodes-langchain.outputparserautofixing, n8n-nodes-langchain.outputparserstructured, executecommand | 🔴 High | [📚 Auto-generate documentation for n8n workflows with GPT and Docsify.json](workflows/📚 Auto-generate documentation for n8n workflows with GPT and Docsify.json) |
| Docsify example | automate | n8n-nodes-langchain.outputparserautofixing, n8n-nodes-langchain.outputparserstructured, executecommand | 🔴 High | [VY4TXYGmqth57Een_Docsify_example.json](workflows/VY4TXYGmqth57Een_Docsify_example.json) |
| Dsp agent | automate | n8n-nodes-langchain.memorybufferwindow, airtable, n8n-nodes-langchain.calculator | 🔴 High | [Dsp_agent (1).json](workflows/Dsp_agent (1).json) |
| Dynamically switch between LLMs Template | automate | n8n-nodes-langchain.chainllm, n8n-nodes-langchain.chat, n8n-nodes-langchain.code | 🔴 High | [dQC8kExvbCrovWf0_Dynamically_switch_between_LLMs_Template.json](workflows/dQC8kExvbCrovWf0_Dynamically_switch_between_LLMs_Template.json) |
| Easy Image Captioning with Gemini 1.5 Pro | automate | n8n-nodes-langchain.chainllm, n8n-nodes-langchain.outputparserstructured, httprequest | 🔴 High | [Easy Image Captioning with Gemini 1.5 Pro.json](workflows/Easy Image Captioning with Gemini 1.5 Pro.json) |
| Enhance Customer Chat by Buffering Messages with Twilio and Redis | automate | n8n-nodes-langchain.memorybufferwindow, n8n-nodes-langchain.memorymanager, n8n-nodes-langchain.lmchatopenai | 🔴 High | [Enhance Customer Chat by Buffering Messages with Twilio and Redis.json](workflows/Enhance Customer Chat by Buffering Messages with Twilio and Redis.json) |
| Generating Image Embeddings via Textual Summarisation | automate | n8n-nodes-langchain.vectorstoreinmemory, n8n-nodes-langchain.embeddingsopenai, manual | 🔴 High | [Generating Image Embeddings via Textual Summarisation.json](workflows/Generating Image Embeddings via Textual Summarisation.json) |
| GitLab MR Auto-Review & Risk Assessment | automate | n8n-nodes-langchain.outputparserautofixing, n8n-nodes-langchain.outputparserstructured, gmail | 🔴 High | [jzcvnlV8g6aseE4A_GitLab_MR_Auto-Review_&_Risk_Assessment.json](workflows/jzcvnlV8g6aseE4A_GitLab_MR_Auto-Review_&_Risk_Assessment.json) |
| Github Releases | automate | splitinbatches, slack, datetime | 🔴 High | [ThLx9WKLEujJHrvW_Github_Releases.json](workflows/ThLx9WKLEujJHrvW_Github_Releases.json) |
| Google Calendar Event Reminder | automate | schedule, googlecalendar, n8n-nodes-langchain.lmchatopenai | 🟡 Medium | [SvYHgLmzosuLAe4A_Google_Calendar_Event_Reminder.json](workflows/SvYHgLmzosuLAe4A_Google_Calendar_Event_Reminder.json) |
| Google Doc Summarizer to Google Sheets | automate | n8n-nodes-langchain.calculator, googledocs, n8n-nodes-langchain.wikipedia | 🟡 Medium | [Summarize the New Documents from Google Drive and Save Summary in Google Sheet.json](workflows/Summarize the New Documents from Google Drive and Save Summary in Google Sheet.json) |
| Google Drive Automation | automate | n8n-nodes-langchain.chat, n8n-nodes-langchain.embeddingsgooglegemini, n8n-nodes-langchain.textsplitterrecursivecharactertextsplitter | 🔴 High | [lC8xkfCSTjIiUhpk_Google_Drive_Automation.json](workflows/lC8xkfCSTjIiUhpk_Google_Drive_Automation.json) |
| Google Maps FULL | automate | n8n-nodes-langchain.memorybufferwindow, n8n-nodes-langchain.chat, httprequest | 🔴 High | [qhZvZVCoV3HLjRkq_Google_Maps_FULL.json](workflows/qhZvZVCoV3HLjRkq_Google_Maps_FULL.json) |
| Google Site Index - sitemap.xml example | automate | splitinbatches, httprequest, schedule | 🔴 High | [7i2RqqCYaKHUt4n3_Google_Site_Index_-_sitemap.xml_example.json](workflows/7i2RqqCYaKHUt4n3_Google_Site_Index_-_sitemap.xml_example.json) |
| Gratitude Jar Reminder | automate | n8n-nodes-langchain.lmchatazureopenai, n8n-nodes-langchain.chainllm, httprequest | 🟡 Medium | [Sebvr1R2t4zkAg1V_Gratitude_Jar_Reminder.json](workflows/Sebvr1R2t4zkAg1V_Gratitude_Jar_Reminder.json) |
| HDW Lead Geländewagen | automate | n8n-nodes-langchain.memorybufferwindow, splitinbatches, n8n-nodes-langchain.outputparserstructured | 🔴 High | [piapgd2e6zmzFxAq_HDW_Lead_Geländewagen.json](workflows/piapgd2e6zmzFxAq_HDW_Lead_Geländewagen.json) |
| HR & IT Helpdesk Chatbot with Audio Transcription | automate | n8n-nodes-langchain.vectorstore, n8n-nodes-langchain.memorypostgreschat, httprequest | 🔴 High | [HR & IT Helpdesk Chatbot with Audio Transcription.json](workflows/HR & IT Helpdesk Chatbot with Audio Transcription.json) |
| HR & IT Helpdesk Chatbot with Audio Transcription | automate | n8n-nodes-langchain.vectorstore, n8n-nodes-langchain.memorypostgreschat, httprequest | 🔴 High | [zmgSshZ5xESr3ozl_HR_&_IT_Helpdesk_Chatbot_with_Audio_Transcription.json](workflows/zmgSshZ5xESr3ozl_HR_&_IT_Helpdesk_Chatbot_with_Audio_Transcription.json) |
| Hacker News Throwback Machine - See What Was Hot on This Day, Every Year! | automate | n8n-nodes-langchain.chainllm, httprequest, schedule | 🔴 High | [Hacker News Throwback Machine - See What Was Hot on This Day, Every Year!.json](workflows/Hacker News Throwback Machine - See What Was Hot on This Day, Every Year!.json) |
| Hacker News to Video Template - AlexK1919 | automate | n8n-nodes-langchain.outputparserstructured, httprequest, googledrive | 🔴 High | [Hacker News to Video Content.json](workflows/Hacker News to Video Content.json) |
| Hacker News to Video Template - AlexK1919 | automate | n8n-nodes-langchain.outputparserstructured, httprequest, googledrive | 🔴 High | [744G7emgZe0pXaPB_Hacker_News_to_Video_Template_-_AlexK1919.json](workflows/744G7emgZe0pXaPB_Hacker_News_to_Video_Template_-_AlexK1919.json) |
| Hugging Face  to Notion | automate | splitinbatches, httprequest, notion | 🟡 Medium | [FU3MrLkaTHmfdG4n_Hugging_Face__to_Notion.json](workflows/FU3MrLkaTHmfdG4n_Hugging_Face__to_Notion.json) |
| Hugging Face to Notion | automate | splitinbatches, httprequest, notion | 🟡 Medium | [Analyse papers from Hugging Face with AI and store them in Notion.json](workflows/Analyse papers from Hugging Face with AI and store them in Notion.json) |
| Image Generation API | automate | webhook, n8n-nodes-langchain.openai, respondtowebhook | 🟡 Medium | [wDD4XugmHIvx3KMT_Image_Generation_API.json](workflows/wDD4XugmHIvx3KMT_Image_Generation_API.json) |
| Image Generation API | automate | webhook, n8n-nodes-langchain.openai, respondtowebhook | 🟡 Medium | [Configure your own Image Creation API Using OpenAI DALLE-3.json](workflows/Configure your own Image Creation API Using OpenAI DALLE-3.json) |
| InstaTest | automate | n8n-nodes-langchain.memorybufferwindow, webhook, n8n-nodes-langchain.lmchatopenai | 🟡 Medium | [qww129cm4TM9N8Ru_InstaTest.json](workflows/qww129cm4TM9N8Ru_InstaTest.json) |
| InstaTest | automate | n8n-nodes-langchain.memorybufferwindow, webhook, n8n-nodes-langchain.lmchatopenai | 🟡 Medium | [AI agent for Instagram DM_inbox. Manychat + Open AI integration.json](workflows/AI agent for Instagram DM_inbox. Manychat + Open AI integration.json) |
| Intelligent Web Query and Semantic Re-Ranking Flow | automate | n8n-nodes-langchain.outputparserautofixing, n8n-nodes-langchain.chainllm, n8n-nodes-langchain.outputparserstructured | 🔴 High | [Intelligent Web Query and Semantic Re-Ranking Flow using Brave and Google Gemini.json](workflows/Intelligent Web Query and Semantic Re-Ranking Flow using Brave and Google Gemini.json) |
| Intelligent Web Query and Semantic Re-Ranking Flow | automate | n8n-nodes-langchain.outputparserautofixing, n8n-nodes-langchain.chainllm, n8n-nodes-langchain.outputparserstructured | 🔴 High | [wa2uEnSIowqSrHoY_Intelligent_Web_Query_and_Semantic_Re-Ranking_Flow.json](workflows/wa2uEnSIowqSrHoY_Intelligent_Web_Query_and_Semantic_Re-Ranking_Flow.json) |
| Introduction to the HTTP Tool | automate | n8n-nodes-langchain.httprequest, n8n-nodes-langchain.lmchatopenai, manual | 🟡 Medium | [Introduction to the HTTP Tool.json](workflows/Introduction to the HTTP Tool.json) |
| Inverview Scheduler | automate | n8n-nodes-langchain.memorybufferwindow, n8n-nodes-langchain.outputparserstructured, n8n-nodes-langchain.chat | 🔴 High | [bh3H2b654RSYgIm9_Inverview_Scheduler.json](workflows/bh3H2b654RSYgIm9_Inverview_Scheduler.json) |
| Jira Retrospective | automate | n8n-nodes-langchain.memorybufferwindow, googledocs, jira | 🔴 High | [U1xUqDLvBYYSU6EU_Jira_Retrospective.json](workflows/U1xUqDLvBYYSU6EU_Jira_Retrospective.json) |
| LinkedIn Profile Finder via Form using Bright Data & GPT-4o-mini | automate | emailsend, form, limit | 🔴 High | [nmVATBvrztDxZX6z_LinkedIn_Profile_Finder_via_Form_using_Bright_Data_&_GPT-4o-mini.json](workflows/nmVATBvrztDxZX6z_LinkedIn_Profile_Finder_via_Form_using_Bright_Data_&_GPT-4o-mini.json) |
| LinkedIn Web Scraping with Bright Data MCP Server & Google Gemini | automate | httprequest, readwritefile, n8n-nodes-langchain.informationextractor | 🔴 High | [D2RkoPZlkKFRUrNu_LinkedIn_Web_Scraping_with_Bright_Data_MCP_Server_&_Google_Gemini.json](workflows/D2RkoPZlkKFRUrNu_LinkedIn_Web_Scraping_with_Bright_Data_MCP_Server_&_Google_Gemini.json) |
| Load Prompts from Github Repo and auto populate n8n expressions | automate | stopanderror, manual, github | 🔴 High | [Fetch Dynamic Prompts from GitHub and Auto-Populate n8n Expressions in Prompt.json](workflows/Fetch Dynamic Prompts from GitHub and Auto-Populate n8n Expressions in Prompt.json) |
| Load Prompts from Github Repo and auto populate n8n expressions | automate | stopanderror, manual, github | 🔴 High | [QyMyf3zraY0wxXDf_Load_Prompts_from_Github_Repo_and_auto_populate_n8n_expressions.json](workflows/QyMyf3zraY0wxXDf_Load_Prompts_from_Github_Repo_and_auto_populate_n8n_expressions.json) |
| MCP_SUPABASE_AGENT | automate | n8n-nodes-langchain.vectorstoresupabase, n8n-nodes-langchain.mcp, n8n-nodes-langchain.embeddingsopenai | 🔴 High | [oowUGM7ey6gWxzEG_MCP_SUPABASE_AGENT.json](workflows/oowUGM7ey6gWxzEG_MCP_SUPABASE_AGENT.json) |
| MongoDB Agent | automate | n8n-nodes-langchain.memorybufferwindow, mongodb, n8n-nodes-langchain.chat | 🟡 Medium | [22PddLUgcjSJbT1w_MongoDB_Agent.json](workflows/22PddLUgcjSJbT1w_MongoDB_Agent.json) |
| MongoDB Agent | automate | n8n-nodes-langchain.memorybufferwindow, mongodb, n8n-nodes-langchain.chat | 🟡 Medium | [MongoDB AI Agent - Intelligent Movie Recommendations.json](workflows/MongoDB AI Agent - Intelligent Movie Recommendations.json) |
| My workflow | automate | splitinbatches, n8n-nodes-langchain.chainllm, reddit | 🔴 High | [h2uiciRa1D3ntSTT_My_workflow.json](workflows/h2uiciRa1D3ntSTT_My_workflow.json) |
| My workflow 3 | automate | n8n-nodes-langchain.chainretrievalqa, httprequest, n8n-nodes-langchain.informationextractor | 🔴 High | [cGNK44mkCzIh4113_My_workflow_3.json](workflows/cGNK44mkCzIh4113_My_workflow_3.json) |
| My workflow 6 | automate | slack, n8n-nodes-langchain.chainllm, webhook | 🟡 Medium | [Slack slash commands AI Chat Bot.json](workflows/Slack slash commands AI Chat Bot.json) |
| My workflow 6 | automate | slack, n8n-nodes-langchain.chainllm, webhook | 🟡 Medium | [PGLFPj5y01s26rE1_My_workflow_6.json](workflows/PGLFPj5y01s26rE1_My_workflow_6.json) |
| OpenSea Analytics Agent Tool | automate | n8n-nodes-langchain.memorybufferwindow, n8n-nodes-langchain.httprequest, n8n-nodes-langchain.lmchatopenai | 🟡 Medium | [yRMCUm6oJEMknhbw_OpenSea_Analytics_Agent_Tool.json](workflows/yRMCUm6oJEMknhbw_OpenSea_Analytics_Agent_Tool.json) |
| OpenSea Marketplace Agent Tool | automate | n8n-nodes-langchain.memorybufferwindow, n8n-nodes-langchain.httprequest, n8n-nodes-langchain.lmchatopenai | 🔴 High | [brRSLvIkYp3mLq0K_OpenSea_Marketplace_Agent_Tool.json](workflows/brRSLvIkYp3mLq0K_OpenSea_Marketplace_Agent_Tool.json) |
| OpenSea NFT Agent Tool | automate | n8n-nodes-langchain.memorybufferwindow, n8n-nodes-langchain.httprequest, n8n-nodes-langchain.lmchatopenai | 🔴 High | [ZBH1ExE58wsoodkZ_OpenSea_NFT_Agent_Tool.json](workflows/ZBH1ExE58wsoodkZ_OpenSea_NFT_Agent_Tool.json) |
| Optimize Prompt | automate | n8n-nodes-langchain.memorybufferwindow, n8n-nodes-langchain.lmchatopenai, n8n-nodes-langchain.agent | 🟡 Medium | [heyKyETy1uK0xoX4_Optimize_Prompt.json](workflows/heyKyETy1uK0xoX4_Optimize_Prompt.json) |
| Outlook | automate | microsoftoutlook, n8n-nodes-langchain.lmchatopenai, n8n-nodes-langchain.agent | 🟡 Medium | [mqindLlOy0A0e5aA_Outlook.json](workflows/mqindLlOy0A0e5aA_Outlook.json) |
| POC - Chatbot Order by Sheet Data | automate | n8n-nodes-langchain.memorybufferwindow, n8n-nodes-langchain.calculator, n8n-nodes-langchain.chat | 🟡 Medium | [5Y8QXJ3N67wnmR2R_POC_-_Chatbot_Order_by_Sheet_Data.json](workflows/5Y8QXJ3N67wnmR2R_POC_-_Chatbot_Order_by_Sheet_Data.json) |
| Parents smart bot | automate | n8n-nodes-langchain.memorybufferwindow, n8n-nodes-langchain.calculator, n8n-nodes-langchain.wikipedia | 🔴 High | [Parents_smart_bot (2).json](workflows/Parents_smart_bot (2).json) |
| Personal Assistant MCP server | automate | n8n-nodes-langchain.memorybufferwindow, googlesheets, n8n-nodes-langchain.chat | 🔴 High | [KhUd3rHKtZAImiXZ_Personal_Assistant_MCP_server.json](workflows/KhUd3rHKtZAImiXZ_Personal_Assistant_MCP_server.json) |
| Personal Portfolio Resume CV Chatbot | automate | n8n-nodes-langchain.memorybufferwindow, n8n-nodes-langchain.vectorstore, respondtowebhook | 🔴 High | [hzwyrm761fxBLiG8_Personal_Portfolio_Resume_CV_Chatbot.json](workflows/hzwyrm761fxBLiG8_Personal_Portfolio_Resume_CV_Chatbot.json) |
| Play with Spotify from Telegram | automate | telegram, telegram, n8n-nodes-langchain.openai | 🔴 High | [Telegram to Spotify with OpenAI.json](workflows/Telegram to Spotify with OpenAI.json) |
| Play with Spotify from Telegram | automate | telegram, telegram, n8n-nodes-langchain.openai | 🔴 High | [F7CfIF10XjXhqbGb_Play_with_Spotify_from_Telegram.json](workflows/F7CfIF10XjXhqbGb_Play_with_Spotify_from_Telegram.json) |
| Podcast Digest | automate | itemlists, n8n-nodes-langchain.chainllm, n8n-nodes-langchain.outputparserstructured | 🔴 High | [AI_ Summarize podcast episode and enhance using Wikipedia.json](workflows/AI_ Summarize podcast episode and enhance using Wikipedia.json) |
| Post New YouTube Videos to X | automate | schedule, twitter, n8n-nodes-langchain.openai | 🟡 Medium | [O9FXr8iXzhSgYKaL_Post_New_YouTube_Videos_to_X.json](workflows/O9FXr8iXzhSgYKaL_Post_New_YouTube_Videos_to_X.json) |
| Post New YouTube Videos to X | automate | schedule, twitter, n8n-nodes-langchain.openai | 🟡 Medium | [Post New YouTube Videos to X.json](workflows/Post New YouTube Videos to X.json) |
| Prepare CSV files with GPT-4 | automate | splitinbatches, spreadsheetfile, itemlists | 🟡 Medium | [6FSx5OMVxp8Ldg8A_Prepare_CSV_files_with_GPT-4.json](workflows/6FSx5OMVxp8Ldg8A_Prepare_CSV_files_with_GPT-4.json) |
| Prepare CSV files with GPT-4 | automate | splitinbatches, spreadsheetfile, itemlists | 🟡 Medium | [Prepare CSV files with GPT-4Prepare CSV files with GPT-4.json](workflows/Prepare CSV files with GPT-4Prepare CSV files with GPT-4.json) |
| Prod: Notion to Vector Store - Dimension 768 | automate | n8n-nodes-langchain.textsplittertokensplitter, n8n-nodes-langchain.embeddingsgooglegemini, notion | 🟡 Medium | [Notion to Pinecone Vector Store Integration.json](workflows/Notion to Pinecone Vector Store Integration.json) |
| Prompt-based Object Detection with Gemini 2.0 | automate | httprequest, manual, editimage | 🟡 Medium | [Prompt-based Object Detection with Gemini 2.0.json](workflows/Prompt-based Object Detection with Gemini 2.0.json) |
| Publish Videos & Images - Blotato | automate | httprequest, manual, airtable | 🔴 High | [8Sbrzc7Au3ZGf62p_Publish_Videos_&_Images_-_Blotato.json](workflows/8Sbrzc7Au3ZGf62p_Publish_Videos_&_Images_-_Blotato.json) |
| Qdrant Vector Database Embedding Pipeline | automate | splitinbatches, n8n-nodes-langchain.textsplittercharactertextsplitter, ftp | 🔴 High | [YoUP55V241b9F2ze_Qdrant_Vector_Database_Embedding_Pipeline.json](workflows/YoUP55V241b9F2ze_Qdrant_Vector_Database_Embedding_Pipeline.json) |
| RAG Workflow For Company Documents stored in Google Drive | automate | n8n-nodes-langchain.memorybufferwindow, n8n-nodes-langchain.vectorstore, googledrive | 🔴 High | [RAG Chatbot for Company Documents using Google Drive and Gemini.json](workflows/RAG Chatbot for Company Documents using Google Drive and Gemini.json) |
| RAG Workflow For Company Documents stored in Google Drive | automate | n8n-nodes-langchain.memorybufferwindow, n8n-nodes-langchain.vectorstore, googledrive | 🔴 High | [7cXvgkl9170QXzT2_RAG_Workflow_For_Company_Documents_stored_in_Google_Drive.json](workflows/7cXvgkl9170QXzT2_RAG_Workflow_For_Company_Documents_stored_in_Google_Drive.json) |
| RAG on living data | automate | splitinbatches, n8n-nodes-langchain.chainretrievalqa, supabase | 🔴 High | [Upsert huge documents in a vector store with Supabase and Notion.json](workflows/Upsert huge documents in a vector store with Supabase and Notion.json) |
| RAG on living data | automate | splitinbatches, n8n-nodes-langchain.chainretrievalqa, supabase | 🔴 High | [JxFP8FJ2W7e4Kmqn_RAG_on_living_data.json](workflows/JxFP8FJ2W7e4Kmqn_RAG_on_living_data.json) |
| RAG:Context-Aware Chunking \| Google Drive to Pinecone via OpenRouter & Gemini | automate | splitinbatches, n8n-nodes-langchain.embeddingsgooglegemini, n8n-nodes-langchain.lmchatopenrouter | 🔴 High | [RAG_Context-Aware Chunking _ Google Drive to Pinecone via OpenRouter & Gemini.json](workflows/RAG_Context-Aware Chunking _ Google Drive to Pinecone via OpenRouter & Gemini.json) |
| Reservation Medcin | automate | n8n-nodes-langchain.memorybufferwindow, googlesheets, n8n-nodes-langchain.chat | 🟡 Medium | [my335cY3wVwMqvqy_Reservation_Medcin.json](workflows/my335cY3wVwMqvqy_Reservation_Medcin.json) |
| Resume Screening & Behavioral Interviews with Gemini, Elevenlabs, & Notion ATS copy | automate | n8n-nodes-langchain.outputparserstructured, httprequest, n8n-nodes-langchain.informationextractor | 🔴 High | [EnfvHdczSXHN8vNv_Resume_Screening_&_Behavioral_Interviews_with_Gemini,_Elevenlabs,_&_Notion_ATS_copy.json](workflows/EnfvHdczSXHN8vNv_Resume_Screening_&_Behavioral_Interviews_with_Gemini,_Elevenlabs,_&_Notion_ATS_copy.json) |
| SEO Blog Generator with GPT-4o, Perplexity, and Telegram Integration | automate | n8n-nodes-langchain.memorybufferwindow, n8n-nodes-langchain.outputparserstructured, n8n-nodes-langchain.lmchatopenai | 🔴 High | [Xfz2YRxH6qFfpqHw_SEO_Blog_Generator_with_GPT-4o,_Perplexity,_and_Telegram_Integration.json](workflows/Xfz2YRxH6qFfpqHw_SEO_Blog_Generator_with_GPT-4o,_Perplexity,_and_Telegram_Integration.json) |
| SHEETS RAG | automate | postgres, n8n-nodes-langchain.manualchat, n8n-nodes-langchain.lmchatgooglegemini | 🔴 High | [7gRbzEzCuOzQKn4M_SHEETS_RAG.json](workflows/7gRbzEzCuOzQKn4M_SHEETS_RAG.json) |
| SQL agent with memory | automate | n8n-nodes-langchain.memorybufferwindow, n8n-nodes-langchain.chat, httprequest | 🔴 High | [AQJ6QnF2yVdCWMnx_SQL_agent_with_memory.json](workflows/AQJ6QnF2yVdCWMnx_SQL_agent_with_memory.json) |
| SQL agent with memory | automate | n8n-nodes-langchain.memorybufferwindow, n8n-nodes-langchain.chat, httprequest | 🔴 High | [Talk to your SQLite database with a LangChain AI Agent.json](workflows/Talk to your SQLite database with a LangChain AI Agent.json) |
| Save New Sales Opportunities | automate | gmail, n8n-nodes-langchain.lmopenai, n8n-nodes-langchain.chainsummarization | 🟢 Low | [NPGAfBzz4nv8lTpl_Save_New_Sales_Opportunities.json](workflows/NPGAfBzz4nv8lTpl_Save_New_Sales_Opportunities.json) |
| SearchApi Youtube Video Summary | automate | n8n-nodes-langchain.chainsummarization, manual, n8n-nodes-langchain.lmchatopenai | 🟡 Medium | [MkZ77sIELEO2kQx1_SearchApi_Youtube_Video_Summary.json](workflows/MkZ77sIELEO2kQx1_SearchApi_Youtube_Video_Summary.json) |
| Simple LinkedIn profile collector | automate | nocodb, httprequest, manual | 🔴 High | [W5cevjhP3xIQdMhT_Simple_LinkedIn_profile_collector.json](workflows/W5cevjhP3xIQdMhT_Simple_LinkedIn_profile_collector.json) |
| Speech Support Workflow | automate | n8n-nodes-langchain.memorybufferwindow, telegram, n8n-nodes-langchain.lmchatgooglegemini | 🔴 High | [Fdbft9uw8mLGXMoE_Speech_Support_Workflow.json](workflows/Fdbft9uw8mLGXMoE_Speech_Support_Workflow.json) |
| Speed Up Social Media Banners With BannerBear.com | automate | httprequest, bannerbear, n8n-nodes-langchain.openai | 🔴 High | [Speed Up Social Media Banners With BannerBear.com.json](workflows/Speed Up Social Media Banners With BannerBear.com.json) |
| Stock Q&A Workflow | automate | n8n-nodes-langchain.chainretrievalqa, n8n-nodes-langchain.documentbinaryinputloader, n8n-nodes-langchain.embeddingsopenai | 🔴 High | [AI Crew to Automate Fundamental Stock Analysis - Q&A Workflow.json](workflows/AI Crew to Automate Fundamental Stock Analysis - Q&A Workflow.json) |
| Streamline Your Zoom Meetings with Secure, Automated Stripe Payments | automate | gmail, httprequest, stripe | 🔴 High | [2DT5BW5tOdy87AUl_Streamline_Your_Zoom_Meetings_with_Secure,_Automated_Stripe_Payments.json](workflows/2DT5BW5tOdy87AUl_Streamline_Your_Zoom_Meetings_with_Secure,_Automated_Stripe_Payments.json) |
| Summarize YouTube Videos & Chat About Content with GPT-4o-mini via Telegram | automate | n8n-nodes-langchain.memorybufferwindow, n8n-nodes-langchain.chainllm, googledocs | 🔴 High | [KgoL0qrLYZUJFuAS_Summarize_YouTube_Videos_&_Chat_About_Content_with_GPT-4o-mini_via_Telegram.json](workflows/KgoL0qrLYZUJFuAS_Summarize_YouTube_Videos_&_Chat_About_Content_with_GPT-4o-mini_via_Telegram.json) |
| Summarize YouTube Videos from Transcript | automate | n8n-nodes-langchain.chainsummarization, httprequest, n8n-nodes-langchain.lmchatopenai | 🟡 Medium | [Summarize YouTube Videos from Transcript.json](workflows/Summarize YouTube Videos from Transcript.json) |
| Supabase Setup Postgres | automate | supabase, n8n-nodes-langchain.memorypostgreschat, n8n-nodes-langchain.lmchatgooglegemini | 🟡 Medium | [gUx6hY0bOoReluxE_Supabase_Setup_Postgres.json](workflows/gUx6hY0bOoReluxE_Supabase_Setup_Postgres.json) |
| Tech Radar | automate | n8n-nodes-langchain.lmchatanthropic, googledrive, n8n-nodes-langchain.textsplitterrecursivecharactertextsplitter | 🔴 High | [dLKIZxM6c0lRVbjb_Tech_Radar.json](workflows/dLKIZxM6c0lRVbjb_Tech_Radar.json) |
| Telegram Chat with Buffering | automate | supabase, n8n-nodes-langchain.memorypostgreschat, sort | 🔴 High | [DnHvQ3KL8v8r5L5Z_Telegram_Chat_with_Buffering.json](workflows/DnHvQ3KL8v8r5L5Z_Telegram_Chat_with_Buffering.json) |
| Telegram ChatBot with multiple sessions | automate | n8n-nodes-langchain.memorybufferwindow, n8n-nodes-langchain.chainllm, n8n-nodes-langchain.chainsummarization | 🔴 High | [A7dRnMf9WybO8O02_Telegram_ChatBot_with_multiple_sessions.json](workflows/A7dRnMf9WybO8O02_Telegram_ChatBot_with_multiple_sessions.json) |
| Telegram RAG pdf | automate | n8n-nodes-langchain.chainretrievalqa, stopanderror, n8n-nodes-langchain.embeddingsopenai | 🔴 High | [5Ycrm1MuK8htwd96_Telegram_RAG_pdf.json](workflows/5Ycrm1MuK8htwd96_Telegram_RAG_pdf.json) |
| Telegram RAG pdf | automate | n8n-nodes-langchain.chainretrievalqa, stopanderror, n8n-nodes-langchain.embeddingsopenai | 🔴 High | [Telegram chat with PDF.json](workflows/Telegram chat with PDF.json) |
| Test Webhooks in n8n Without Changing WEBHOOK_URL (PostBin & BambooHR Example) | automate | n8n-nodes-langchain.outputparserautofixing, n8n-nodes-langchain.outputparserstructured, httprequest | 🔴 High | [sB6dC0GZ7zZHuMGF_Test_Webhooks_in_n8n_Without_Changing_WEBHOOK_URL_(PostBin_&_BambooHR_Example).json](workflows/sB6dC0GZ7zZHuMGF_Test_Webhooks_in_n8n_Without_Changing_WEBHOOK_URL_(PostBin_&_BambooHR_Example).json) |
| Testing Mulitple Local LLM with LM Studio | automate | n8n-nodes-langchain.chainllm, datetime, n8n-nodes-langchain.chat | 🔴 High | [WulUYgcXvako9hBy_Testing_Mulitple_Local_LLM_with_LM_Studio.json](workflows/WulUYgcXvako9hBy_Testing_Mulitple_Local_LLM_with_LM_Studio.json) |
| Testing Mulitple Local LLM with LM Studio | automate | n8n-nodes-langchain.chainllm, datetime, n8n-nodes-langchain.chat | 🔴 High | [🚀 Local Multi-LLM Testing & Performance Tracker.json](workflows/🚀 Local Multi-LLM Testing & Performance Tracker.json) |
| Text automations using Apple Shortcuts | automate | webhook, n8n-nodes-langchain.openai, respondtowebhook | 🟡 Medium | [Text automations using Apple Shortcuts.json](workflows/Text automations using Apple Shortcuts.json) |
| Text automations using Apple Shortcuts (1) | automate | webhook, n8n-nodes-langchain.openai, respondtowebhook | 🟡 Medium | [Text automations using Apple Shortcuts (1).json](workflows/Text automations using Apple Shortcuts (1).json) |
| TopSourcer - Finds LinkedIn Profiles using natural language | automate | n8n-nodes-langchain.chat, httprequest, googlesheets | 🔴 High | [UsBaGY83vnyZjRoB_TopSourcer_-_Finds_LinkedIn_Profiles_using_natural_language.json](workflows/UsBaGY83vnyZjRoB_TopSourcer_-_Finds_LinkedIn_Profiles_using_natural_language.json) |
| Travel AssistantAgent | automate | n8n-nodes-langchain.memorymongodbchat, n8n-nodes-langchain.chat, n8n-nodes-langchain.embeddingsopenai | 🔴 High | [znRwva47HzXesOYk_Travel_AssistantAgent.json](workflows/znRwva47HzXesOYk_Travel_AssistantAgent.json) |
| Ultimate Personal Assistant | automate | n8n-nodes-langchain.memorybufferwindow, n8n-nodes-langchain.calculator, n8n-nodes-langchain.httprequest | 🔴 High | [Ultimate_Personal_Assistant.json](workflows/Ultimate_Personal_Assistant.json) |
| Use XMLRPC via HttpRequest-node to post on Wordpress.com | automate | httprequest, manual, xml | 🟡 Medium | [yPIST7l13huQEjY5_Use_XMLRPC_via_HttpRequest-node_to_post_on_Wordpress.com.json](workflows/yPIST7l13huQEjY5_Use_XMLRPC_via_HttpRequest-node_to_post_on_Wordpress.com.json) |
| Use any LLM-Model via OpenRouter | automate | n8n-nodes-langchain.memorybufferwindow, n8n-nodes-langchain.chat, n8n-nodes-langchain.lmchatopenai | 🟡 Medium | [VhN3CX6QPBkX77pZ_Use_any_LLM-Model_via_OpenRouter.json](workflows/VhN3CX6QPBkX77pZ_Use_any_LLM-Model_via_OpenRouter.json) |
| Use any LLM-Model via OpenRouter | automate | n8n-nodes-langchain.memorybufferwindow, n8n-nodes-langchain.chat, n8n-nodes-langchain.lmchatopenai | 🟡 Medium | [Use OpenRouter in n8n versions _1.78.json](workflows/Use OpenRouter in n8n versions _1.78.json) |
| Vector DB Loader from Google Drive | automate | splitinbatches, schedule, n8n-nodes-langchain.embeddingsopenai | 🔴 High | [WceMkVib0VLlF1BZ_Vector_DB_Loader_from_Google_Drive.json](workflows/WceMkVib0VLlF1BZ_Vector_DB_Loader_from_Google_Drive.json) |
| Venafi Cloud Slack Cert Bot | automate | venafitlsprotectcloud, slack, httprequest | 🔴 High | [Venafi Cloud Slack Cert Bot.json](workflows/Venafi Cloud Slack Cert Bot.json) |
| Whisper Transkription copy | automate | notion, googledrive, n8n-nodes-langchain.openai | 🟡 Medium | [Transcribe Audio Files, Summarize with GPT-4, and Store in Notion.json](workflows/Transcribe Audio Files, Summarize with GPT-4, and Store in Notion.json) |
| Whisper Transkription copy | automate | notion, googledrive, n8n-nodes-langchain.openai | 🟡 Medium | [TWcBOEMLFs7e6KjP_Whisper_Transkription_copy.json](workflows/TWcBOEMLFs7e6KjP_Whisper_Transkription_copy.json) |
| WordPress Contact Form (CF7) Responses and Classification | automate | n8n-nodes-langchain.chainllm, n8n-nodes-langchain.outputparserstructured, gmail | 🔴 High | [fvgP264GysfRJXdr_WordPress_Contact_Form_(CF7)_Responses_and_Classification.json](workflows/fvgP264GysfRJXdr_WordPress_Contact_Form_(CF7)_Responses_and_Classification.json) |
| Workflow Results to Markdown Notes in Your Obsidian Vault, via Google Drive | automate | n8n-nodes-langchain.outputparserstructured, n8n-nodes-langchain.lmchatopenai, n8n-nodes-langchain.agent | 🔴 High | [3wbxkdT6hilhq0Na_Workflow_Results_to_Markdown_Notes_in_Your_Obsidian_Vault,_via_Google_Drive.json](workflows/3wbxkdT6hilhq0Na_Workflow_Results_to_Markdown_Notes_in_Your_Obsidian_Vault,_via_Google_Drive.json) |
| XML Conversion | automate | xml, manual | 🟢 Low | [3_XML_Conversion.json](workflows/3_XML_Conversion.json) |
| YT New Video Upload | automate | httprequest, youtube, n8n-nodes-langchain.lmchatgooglegemini | 🔴 High | [gIZpJgLpUgdoNNDZ_YT_New_Video_Upload.json](workflows/gIZpJgLpUgdoNNDZ_YT_New_Video_Upload.json) |
| YouTube Video Transcriber | automate | n8n-nodes-langchain.chat, httprequest, n8n-nodes-langchain.openai | 🔴 High | [Iz8TMdlc6JhaKkd9_YouTube_Video_Transcriber.json](workflows/Iz8TMdlc6JhaKkd9_YouTube_Video_Transcriber.json) |
| YouTube to X Post- AlexK1919 | automate | googlesheets, n8n-nodes-langchain.calculator, slack | 🔴 High | [AuwhspweKSACE1WQ_YouTube_to_X_Post-_AlexK1919.json](workflows/AuwhspweKSACE1WQ_YouTube_to_X_Post-_AlexK1919.json) |
| Youtube Discord Bot | automate | n8n-nodes-langchain.memorybufferwindow, webhook, n8n-nodes-langchain.lmchatgooglegemini | 🟡 Medium | [OqfQNcgTqUK7UvZG_Youtube_Discord_Bot.json](workflows/OqfQNcgTqUK7UvZG_Youtube_Discord_Bot.json) |
| Youtube_Automation | automate | splitinbatches, httprequest, schedule | 🔴 High | [wLbJ7rE6vQzizCp2_Youtube_Automation.json](workflows/wLbJ7rE6vQzizCp2_Youtube_Automation.json) |
| agente | automate | googletasks, telegram, n8n-nodes-langchain.memorypostgreschat | 🔴 High | [6LeAm5UyENgTdwkv_agente.json](workflows/6LeAm5UyENgTdwkv_agente.json) |
| dgBdnnnY0622JwGy_workflow_dgBdnnnY0622JwGy | automate | n8n-nodes-langchain.outputparserstructured, gmail, manual | 🔴 High | [dgBdnnnY0622JwGy_workflow_dgBdnnnY0622JwGy.json](workflows/dgBdnnnY0622JwGy_workflow_dgBdnnnY0622JwGy.json) |
| google drive to instagram, tiktok and youtube | automate | error, httprequest, readbinaryfile | 🔴 High | [9nBQ1BfwxLhuzTcK_google_drive_to_instagram,_tiktok_and_youtube.json](workflows/9nBQ1BfwxLhuzTcK_google_drive_to_instagram,_tiktok_and_youtube.json) |
| lemlist __ GPT-3_ Supercharge your sales workflows | automate | N/A | 🟢 Low | [lemlist __ GPT-3_ Supercharge your sales workflows.json](workflows/lemlist __ GPT-3_ Supercharge your sales workflows.json) |
| modelo do chatbot | automate | mysql, n8n-nodes-langchain.memorypostgreschat, n8n-nodes-langchain.chat | 🟡 Medium | [Chat Assistant (OpenAI assistant) with Postgres Memory And API Calling Capabalities.json](workflows/Chat Assistant (OpenAI assistant) with Postgres Memory And API Calling Capabalities.json) |
| modelo do chatbot | automate | mysql, n8n-nodes-langchain.memorypostgreschat, n8n-nodes-langchain.chat | 🟡 Medium | [BMI5WkmyU8nZqfII_modelo_do_chatbot.json](workflows/BMI5WkmyU8nZqfII_modelo_do_chatbot.json) |
| n8n Graphic Design Team | automate | n8n-nodes-langchain.chainllm, n8n-nodes-langchain.outputparserstructured, gmail | 🔴 High | [tnRYt0kDGMO9BBFd_n8n_Graphic_Design_Team.json](workflows/tnRYt0kDGMO9BBFd_n8n_Graphic_Design_Team.json) |
| piepdrive-test | automate | pipedrive, pipedrive, slack | 🟡 Medium | [Enrich Pipedrive_s Organization Data with OpenAI GPT-4o & Notify it in Slack.json](workflows/Enrich Pipedrive_s Organization Data with OpenAI GPT-4o & Notify it in Slack.json) |
| piepdrive-test | automate | pipedrive, pipedrive, slack | 🟡 Medium | [_piepdrive-test.json](workflows/_piepdrive-test.json) |
| spy tool | automate | httprequest, n8n-nodes-langchain.lmchatopenai, n8n-nodes-langchain.agent | 🔴 High | [aOP0D1cAqzGv7Xa8_spy_tool.json](workflows/aOP0D1cAqzGv7Xa8_spy_tool.json) |
| template in store | automate | error, httprequest, readbinaryfile | 🔴 High | [Upload to Instagram and Tiktok from Google Drive.json](workflows/Upload to Instagram and Tiktok from Google Drive.json) |
| template-demo-chatgpt-image-1-with-drive-and-sheet copy | automate | splitinbatches, n8n-nodes-langchain.chat, httprequest | 🔴 High | [0GCQ1fO3d5MBdKmi_template-demo-chatgpt-image-1-with-drive-and-sheet_copy.json](workflows/0GCQ1fO3d5MBdKmi_template-demo-chatgpt-image-1-with-drive-and-sheet_copy.json) |
| youtube chapter generator | automate | n8n-nodes-langchain.chainllm, n8n-nodes-langchain.outputparserstructured, httprequest | 🔴 High | [SCUbdpVPX4USbQmr_youtube_chapter_generator.json](workflows/SCUbdpVPX4USbQmr_youtube_chapter_generator.json) |
| ✍️🌄 Your First Wordpress Content Creator - Quick Start | automate | wordpress, n8n-nodes-langchain.outputparserstructured, httprequest | 🔴 High | [ALg2eFzN4AsHIf3R_✍️🌄_Your_First_Wordpress_Content_Creator_-_Quick_Start.json](workflows/ALg2eFzN4AsHIf3R_✍️🌄_Your_First_Wordpress_Content_Creator_-_Quick_Start.json) |
| ✨🩷Automated Social Media Content Publishing Factory + System Prompt Composition | automate | httprequest, googledrive, telegram | 🔴 High | [0KZs18Ti2KXKoLIr_✨🩷Automated_Social_Media_Content_Publishing_Factory_+_System_Prompt_Composition.json](workflows/0KZs18Ti2KXKoLIr_✨🩷Automated_Social_Media_Content_Publishing_Factory_+_System_Prompt_Composition.json) |
| 🎦💌Advanced YouTube RSS Feed Buddy for Your Favorite Channels | automate | n8n-nodes-langchain.chainllm, gmail, httprequest | 🔴 High | [tHgDFmFyuj6DnP6l_🎦💌Advanced_YouTube_RSS_Feed_Buddy_for_Your_Favorite_Channels.json](workflows/tHgDFmFyuj6DnP6l_🎦💌Advanced_YouTube_RSS_Feed_Buddy_for_Your_Favorite_Channels.json) |
| 🎦🚀 YouTube Video Comment Analysis Agent | automate | gmail, httprequest, markdown | 🔴 High | [d23vz3qcBf6KfuZA_🎦🚀_YouTube_Video_Comment_Analysis_Agent.json](workflows/d23vz3qcBf6KfuZA_🎦🚀_YouTube_Video_Comment_Analysis_Agent.json) |
| 🐋DeepSeek V3 Chat & R1 Reasoning Quick Start | automate | n8n-nodes-langchain.memorybufferwindow, n8n-nodes-langchain.chainllm, n8n-nodes-langchain.chat | 🔴 High | [🐋DeepSeek V3 Chat & R1 Reasoning Quick Start.json](workflows/🐋DeepSeek V3 Chat & R1 Reasoning Quick Start.json) |
| 🐋DeepSeek V3 Chat & R1 Reasoning Quick Start | automate | n8n-nodes-langchain.memorybufferwindow, n8n-nodes-langchain.chainllm, n8n-nodes-langchain.chat | 🔴 High | [IyhH1KHtXidKNSIA_🐋DeepSeek_V3_Chat_&_R1_Reasoning_Quick_Start.json](workflows/IyhH1KHtXidKNSIA_🐋DeepSeek_V3_Chat_&_R1_Reasoning_Quick_Start.json) |
| 💥🛠️Automate Blog Content Creation with GPT-4, Perplexity & WordPress | automate | n8n-nodes-langchain.chat, httprequest, n8n-nodes-langchain.lmchatopenai | 🔴 High | [L1UcBZ9UJvN9gnSb_💥🛠️Automate_Blog_Content_Creation_with_GPT-4,_Perplexity_&_WordPress.json](workflows/L1UcBZ9UJvN9gnSb_💥🛠️Automate_Blog_Content_Creation_with_GPT-4,_Perplexity_&_WordPress.json) |
| 💥🛠️Build a Web Search Chatbot with GPT-4o and MCP Brave Search | automate | n8n-nodes-langchain.memorybufferwindow, n8n-nodes-langchain.chat, n8n-nodes-langchain.lmchatopenai | 🟡 Medium | [6MRJ2tfl8c2f3AuE_💥🛠️Build_a_Web_Search_Chatbot_with_GPT-4o_and_MCP_Brave_Search.json](workflows/6MRJ2tfl8c2f3AuE_💥🛠️Build_a_Web_Search_Chatbot_with_GPT-4o_and_MCP_Brave_Search.json) |
| 📄🛠️PDF2Blog | automate | n8n-nodes-langchain.outputparserstructured, ghost, n8n-nodes-langchain.lmchatopenai | 🔴 High | [dMiUunCiaMsCr1Wu_📄🛠️PDF2Blog.json](workflows/dMiUunCiaMsCr1Wu_📄🛠️PDF2Blog.json) |
| 🔍🛠️Perplexity Researcher to HTML Web Page | automate | n8n-nodes-langchain.chainllm, n8n-nodes-langchain.outputparserstructured, httprequest | 🔴 High | [HnqGW0eq5asKfZxf_🔍🛠️Perplexity_Researcher_to_HTML_Web_Page.json](workflows/HnqGW0eq5asKfZxf_🔍🛠️Perplexity_Researcher_to_HTML_Web_Page.json) |
| 🔐🦙🤖 Private & Local Ollama Self-Hosted LLM Router | automate | n8n-nodes-langchain.memorybufferwindow, n8n-nodes-langchain.chat, n8n-nodes-langchain.lmchatollama | 🔴 High | [Mub5RZI4PAs6TsSP_🔐🦙🤖_Private_&_Local_Ollama_Self-Hosted_LLM_Router.json](workflows/Mub5RZI4PAs6TsSP_🔐🦙🤖_Private_&_Local_Ollama_Self-Hosted_LLM_Router.json) |
| 🗨️Ollama Chat | automate | n8n-nodes-langchain.lmollama, n8n-nodes-langchain.chainllm, n8n-nodes-langchain.chat | 🟡 Medium | [Telr6HU0ltH7s9f7_🗨️Ollama_Chat.json](workflows/Telr6HU0ltH7s9f7_🗨️Ollama_Chat.json) |
| 🗨️Ollama Chat | automate | n8n-nodes-langchain.lmollama, n8n-nodes-langchain.chainllm, n8n-nodes-langchain.chat | 🟡 Medium | [🔐🦙🤖 Private & Local Ollama Self-Hosted AI Assistant.json](workflows/🔐🦙🤖 Private & Local Ollama Self-Hosted AI Assistant.json) |
| 🤓 Conversion Rate Optimizer | automate | n8n-nodes-langchain.lmchatopenai, httprequest, n8n-nodes-langchain.agent | 🟢 Low | [gsra9JToRDftNEvH_🤓_Conversion_Rate_Optimizer.json](workflows/gsra9JToRDftNEvH_🤓_Conversion_Rate_Optimizer.json) |
| 🤖 On-Page SEO Audit | automate | gmail, httprequest, markdown | 🔴 High | [iLpBIRuhpWToO22N_🤖_On-Page_SEO_Audit.json](workflows/iLpBIRuhpWToO22N_🤖_On-Page_SEO_Audit.json) |
| 🤖 Telegram Messaging Agent for Text/Audio/Images | automate | n8n-nodes-langchain.textclassifier, httprequest, webhook | 🔴 High | [🤖 Telegram Messaging Agent for Text_Audio_Images.json](workflows/🤖 Telegram Messaging Agent for Text_Audio_Images.json) |
| 🤖 Telegram Messaging Agent for Text/Audio/Images | automate | n8n-nodes-langchain.textclassifier, httprequest, webhook | 🔴 High | [8jDt77Y4FaV6ARYG_🤖_Telegram_Messaging_Agent_for_Text_Audio_Images.json](workflows/8jDt77Y4FaV6ARYG_🤖_Telegram_Messaging_Agent_for_Text_Audio_Images.json) |
| 🤖Calendar Agent | automate | googlecalendar, n8n-nodes-langchain.lmchatopenai, n8n-nodes-langchain.agent | 🟡 Medium | [__Calendar_Agent.json](workflows/__Calendar_Agent.json) |
| 🤖Contact Agent | automate | airtable, n8n-nodes-langchain.lmchatopenai, n8n-nodes-langchain.agent | 🟡 Medium | [__Contact_Agent.json](workflows/__Contact_Agent.json) |
| 🤖Content Creator Agent | automate | n8n-nodes-langchain.httprequest, n8n-nodes-langchain.lmchatanthropic, n8n-nodes-langchain.agent | 🟡 Medium | [__Content_Creator_Agent.json](workflows/__Content_Creator_Agent.json) |
| Classify lemlist replies using OpenAI and automate reply handling | classify | slack, n8n-nodes-langchain.chainllm, lemlist | 🔴 High | [Classify lemlist replies using OpenAI and automate reply handling.json](workflows/Classify lemlist replies using OpenAI and automate reply handling.json) |
| Classify new bugs in Linear with OpenAI_s GPT-4 and move them to the right team | classify | linear, slack, httprequest | 🔴 High | [Classify new bugs in Linear with OpenAI_s GPT-4 and move them to the right team.json](workflows/Classify new bugs in Linear with OpenAI_s GPT-4 and move them to the right team.json) |
| Create Animated Stories using GPT-4o-mini, Midjourney, Kling and Creatomate API | create | httprequest, manual | 🔴 High | [MfKB97VVSuXMo3Fm_Create_Animated_Stories_using_GPT-4o-mini,_Midjourney,_Kling_and_Creatomate_API.json](workflows/MfKB97VVSuXMo3Fm_Create_Animated_Stories_using_GPT-4o-mini,_Midjourney,_Kling_and_Creatomate_API.json) |
| Insert and retrieve documents | create | n8n-nodes-langchain.chat, httprequest, n8n-nodes-langchain.embeddingsopenai | 🔴 High | [Hjyv9FkH5Oh6Yxw4_Insert_and_retrieve_documents.json](workflows/Hjyv9FkH5Oh6Yxw4_Insert_and_retrieve_documents.json) |
| Supabase Insertion & Upsertion & Retrieval | create | n8n-nodes-langchain.chainretrievalqa, supabase, n8n-nodes-langchain.vectorstoresupabase | 🔴 High | [Supabase Insertion & Upsertion & Retrieval.json](workflows/Supabase Insertion & Upsertion & Retrieval.json) |
| API Schema Extractor | extract | httprequest, n8n-nodes-langchain.informationextractor, googledrive | 🔴 High | [API Schema Extractor.json](workflows/API Schema Extractor.json) |
| Automate Etsy Data Mining with Bright Data Scrape & Google Gemini | extract | splitinbatches, httprequest, readwritefile | 🔴 High | [UuuCIDvTNnloIlvq_Automate_Etsy_Data_Mining_with_Bright_Data_Scrape_&_Google_Gemini.json](workflows/UuuCIDvTNnloIlvq_Automate_Etsy_Data_Mining_with_Bright_Data_Scrape_&_Google_Gemini.json) |
| Automate PDF Image Extraction & Analysis with GPT-4o and Google Drive | extract | httprequest, manual, googledrive | 🔴 High | [NDCN2arRu5tLuP61_Automate_PDF_Image_Extraction_&_Analysis_with_GPT-4o_and_Google_Drive.json](workflows/NDCN2arRu5tLuP61_Automate_PDF_Image_Extraction_&_Analysis_with_GPT-4o_and_Google_Drive.json) |
| Customer Insights with Qdrant, Python and Information Extractor | extract | executeworkflow, httprequest, n8n-nodes-langchain.embeddingsopenai | 🔴 High | [Customer Insights with Qdrant, Python and Information Extractor.json](workflows/Customer Insights with Qdrant, Python and Information Extractor.json) |
| Extract & Summarize Indeed Company Info with Bright Data and Google Gemini | extract | n8n-nodes-langchain.chainllm, httprequest, n8n-nodes-langchain.chainsummarization | 🔴 High | [i89dNLYeOVdTwtcL_Extract_&_Summarize_Indeed_Company_Info_with_Bright_Data_and_Google_Gemini.json](workflows/i89dNLYeOVdTwtcL_Extract_&_Summarize_Indeed_Company_Info_with_Bright_Data_and_Google_Gemini.json) |
| Extract & Summarize Yelp Business Review with Bright Data and Google Gemini | extract | n8n-nodes-langchain.chainllm, n8n-nodes-langchain.outputparserstructured, httprequest | 🔴 High | [cKFPrgXstN3JgdJs_Extract_&_Summarize_Yelp_Business_Review_with_Bright_Data_and_Google_Gemini.json](workflows/cKFPrgXstN3JgdJs_Extract_&_Summarize_Yelp_Business_Review_with_Bright_Data_and_Google_Gemini.json) |
| Extract Amazon Best Seller Electronic Information with Bright Data and Google Gemini | extract | httprequest, n8n-nodes-langchain.informationextractor, manual | 🟡 Medium | [H95uJY2gjSOsxRps_Extract_Amazon_Best_Seller_Electronic_Information_with_Bright_Data_and_Google_Gemini.json](workflows/H95uJY2gjSOsxRps_Extract_Amazon_Best_Seller_Electronic_Information_with_Bright_Data_and_Google_Gemini.json) |
| Extract and process information directly from PDF using Claude and Gemini | extract | httprequest, manual, extractfromfile | 🟡 Medium | [Extract and process information directly from PDF using Claude and Gemini.json](workflows/Extract and process information directly from PDF using Claude and Gemini.json) |
| Extract data from resume and create PDF with Gotenberg | extract | n8n-nodes-langchain.outputparserautofixing, n8n-nodes-langchain.chainllm, n8n-nodes-langchain.outputparserstructured | 🔴 High | [Extract data from resume and create PDF with Gotenberg.json](workflows/Extract data from resume and create PDF with Gotenberg.json) |
| Extract personal data with a self-hosted LLM Mistral NeMo | extract | n8n-nodes-langchain.outputparserautofixing, n8n-nodes-langchain.chainllm, n8n-nodes-langchain.outputparserstructured | 🔴 High | [Extract personal data with self-hosted LLM Mistral NeMo.json](workflows/Extract personal data with self-hosted LLM Mistral NeMo.json) |
| Extract personal data with a self-hosted LLM Mistral NeMo | extract | n8n-nodes-langchain.outputparserautofixing, n8n-nodes-langchain.chainllm, n8n-nodes-langchain.outputparserstructured | 🔴 High | [HMoUOg8J7RzEcslH_Extract_personal_data_with_a_self-hosted_LLM_Mistral_NeMo.json](workflows/HMoUOg8J7RzEcslH_Extract_personal_data_with_a_self-hosted_LLM_Mistral_NeMo.json) |
| Fetch the Most Recent Document from Google Drive | extract | n8n-nodes-langchain.calculator, googledocs, n8n-nodes-langchain.wikipedia | 🟡 Medium | [aswQJmksAOmHmn8c_Fetch_the_Most_Recent_Document_from_Google_Drive.json](workflows/aswQJmksAOmHmn8c_Fetch_the_Most_Recent_Document_from_Google_Drive.json) |
| Google Search Engine Results Page Extraction with Bright Data | extract | n8n-nodes-langchain.chainsummarization, httprequest, n8n-nodes-langchain.httprequest | 🔴 High | [GcSlNHOnN39cPhRA_Google_Search_Engine_Results_Page_Extraction_with_Bright_Data.json](workflows/GcSlNHOnN39cPhRA_Google_Search_Engine_Results_Page_Extraction_with_Bright_Data.json) |
| Google Trend Data Extract, Summarization with Bright Data & Google Gemini | extract | n8n-nodes-langchain.chainllm, gmail, httprequest | 🔴 High | [9Or3kzIEI2tskRyR_Google_Trend_Data_Extract,_Summarization_with_Bright_Data_&_Google_Gemini.json](workflows/9Or3kzIEI2tskRyR_Google_Trend_Data_Extract,_Summarization_with_Bright_Data_&_Google_Gemini.json) |
| HN Who is Hiring Scrape | extract | n8n-nodes-langchain.chainllm, n8n-nodes-langchain.outputparserstructured, httprequest | 🔴 High | [Hacker News Job Listing Scraper and Parser.json](workflows/Hacker News Job Listing Scraper and Parser.json) |
| HN Who is Hiring Scrape | extract | n8n-nodes-langchain.chainllm, n8n-nodes-langchain.outputparserstructured, httprequest | 🔴 High | [0JsHmmyeHw5Ffz5m_HN_Who_is_Hiring_Scrape.json](workflows/0JsHmmyeHw5Ffz5m_HN_Who_is_Hiring_Scrape.json) |
| Line_Chatbot_Extract_Text_from_Pay_Slip_with_Gemini | extract | n8n-nodes-langchain.memorybufferwindow, n8n-nodes-langchain.chainllm, httprequest | 🔴 High | [bPxDenPJ5Ixx0txY_Line_Chatbot_Extract_Text_from_Pay_Slip_with_Gemini.json](workflows/bPxDenPJ5Ixx0txY_Line_Chatbot_Extract_Text_from_Pay_Slip_with_Gemini.json) |
| News Extraction | extract | nocodb, itemlists, httprequest | 🔴 High | [Scrape and summarize posts of a news site without RSS feed using AI and save them to a NocoDB.json](workflows/Scrape and summarize posts of a news site without RSS feed using AI and save them to a NocoDB.json) |
| News Extraction | extract | nocodb, itemlists, httprequest | 🔴 High | [xM8Z5vZVNTNjCySL_News_Extraction.json](workflows/xM8Z5vZVNTNjCySL_News_Extraction.json) |
| Selenium Ultimate Scraper Workflow | extract | httprequest, webhook, n8n-nodes-langchain.lmchatopenai | 🔴 High | [Ultimate Scraper Workflow for n8n.json](workflows/Ultimate Scraper Workflow for n8n.json) |
| Selenium Ultimate Scraper Workflow | extract | httprequest, webhook, n8n-nodes-langchain.lmchatopenai | 🔴 High | [kZ3aL4r7xc96Q7lp_Selenium_Ultimate_Scraper_Workflow.json](workflows/kZ3aL4r7xc96Q7lp_Selenium_Ultimate_Scraper_Workflow.json) |
| Structured Data Extract, Data Mining with Bright Data & Google Gemini | extract | n8n-nodes-langchain.chainllm, httprequest, readwritefile | 🔴 High | [1GOrjyc9mtZCMvCr_Structured_Data_Extract,_Data_Mining_with_Bright_Data_&_Google_Gemini.json](workflows/1GOrjyc9mtZCMvCr_Structured_Data_Extract,_Data_Mining_with_Bright_Data_&_Google_Gemini.json) |
| Summarize Glassdoor Company Info with Google Gemini and Bright Data Web Scraper | extract | httprequest, n8n-nodes-langchain.chainsummarization, n8n-nodes-langchain.lmchatgooglegemini | 🔴 High | [DRjTkkZrfqMbhifO_Summarize_Glassdoor_Company_Info_with_Google_Gemini_and_Bright_Data_Web_Scraper.json](workflows/DRjTkkZrfqMbhifO_Summarize_Glassdoor_Company_Info_with_Google_Gemini_and_Bright_Data_Web_Scraper.json) |
| Survey Insights with Qdrant, Python and Information Extractor | extract | splitinbatches, executeworkflow, httprequest | 🔴 High | [Survey Insights with Qdrant, Python and Information Extractor.json](workflows/Survey Insights with Qdrant, Python and Information Extractor.json) |
| 🔍🛠️ Tavily Search & Extract - Template | extract | n8n-nodes-langchain.chainllm, n8n-nodes-langchain.chat, httprequest | 🔴 High | [QqbYH25we4JDZrZD_🔍🛠️_Tavily_Search_&_Extract_-_Template.json](workflows/QqbYH25we4JDZrZD_🔍🛠️_Tavily_Search_&_Extract_-_Template.json) |
| AI-Generated Summary Block for WordPress Posts - with OpenAI, WordPress, Google Sheets & Slack | generate | splitinbatches, wordpress, slack | 🔴 High | [AhP1Fgv0eCrh9Jxs_AI-Generated_Summary_Block_for_WordPress_Posts_-_with_OpenAI,_WordPress,_Google_Sheets_&_Slack.json](workflows/AhP1Fgv0eCrh9Jxs_AI-Generated_Summary_Block_for_WordPress_Posts_-_with_OpenAI,_WordPress,_Google_Sheets_&_Slack.json) |
| AI-Generated Summary Block for WordPress Posts - with OpenAI, WordPress, Google Sheets & Slack | generate | splitinbatches, wordpress, slack | 🔴 High | [AI-Generated Summary Block for WordPress Posts.json](workflows/AI-Generated Summary Block for WordPress Posts.json) |
| Dynamically generate HTML page from user request using OpenAI Structured Output | generate | httprequest, webhook, html | 🟡 Medium | [Dynamically generate a webpage from user request using OpenAI Structured Output.json](workflows/Dynamically generate a webpage from user request using OpenAI Structured Output.json) |
| Dynamically generate HTML page from user request using OpenAI Structured Output | generate | httprequest, webhook, html | 🟡 Medium | [Dynamically generate a webpage from user request using OpenAI Structured Output (1).json](workflows/Dynamically generate a webpage from user request using OpenAI Structured Output (1).json) |
| Dynamically generate HTML page from user request using OpenAI Structured Output | generate | httprequest, webhook, html | 🟡 Medium | [eXiaTDyKfXpMeyLh_Dynamically_generate_HTML_page_from_user_request_using_OpenAI_Structured_Output.json](workflows/eXiaTDyKfXpMeyLh_Dynamically_generate_HTML_page_from_user_request_using_OpenAI_Structured_Output.json) |
| Generate AI-Ready llms.txt Files from Screaming Frog Website Crawls | generate | n8n-nodes-langchain.textclassifier, converttofile, n8n-nodes-langchain.lmchatopenai | 🔴 High | [_Generate_AI-Ready_llms.txt_Files_from_Screaming_Frog_Website_Crawls.json](workflows/_Generate_AI-Ready_llms.txt_Files_from_Screaming_Frog_Website_Crawls.json) |
| Generate Company Stories from LinkedIn with Bright Data & Google Gemini | generate | httprequest, n8n-nodes-langchain.chainsummarization, n8n-nodes-langchain.lmchatgooglegemini | 🔴 High | [q1DorytEoEw1QLGj_Generate_Company_Stories_from_LinkedIn_with_Bright_Data_&_Google_Gemini.json](workflows/q1DorytEoEw1QLGj_Generate_Company_Stories_from_LinkedIn_with_Bright_Data_&_Google_Gemini.json) |
| Generate Exam Questions | generate | n8n-nodes-langchain.chainretrievalqa, n8n-nodes-langchain.outputparserstructured, httprequest | 🔴 High | [7Qa2mH7PnDxy7Qat_Generate_Exam_Questions.json](workflows/7Qa2mH7PnDxy7Qat_Generate_Exam_Questions.json) |
| Generate Graphic Wallpaper with Midjourney, GPT-4o-mini and Canvas APIs | generate | httprequest, manual | 🔴 High | [mN7jDJoWHtJuyKpS_Generate_Graphic_Wallpaper_with_Midjourney,_GPT-4o-mini_and_Canvas_APIs.json](workflows/mN7jDJoWHtJuyKpS_Generate_Graphic_Wallpaper_with_Midjourney,_GPT-4o-mini_and_Canvas_APIs.json) |
| Generate Instagram Content from Top Trends with AI Image Generation | generate | splitinbatches, postgres, httprequest | 🔴 High | [H7porcmXYj7StO23_Generate_Instagram_Content_from_Top_Trends_with_AI_Image_Generation.json](workflows/H7porcmXYj7StO23_Generate_Instagram_Content_from_Top_Trends_with_AI_Image_Generation.json) |
| Generate Instagram Content from Top Trends with AI Image Generation | generate | splitinbatches, postgres, httprequest | 🔴 High | [Generate Instagram Content from Top Trends with AI Image Generation.json](workflows/Generate Instagram Content from Top Trends with AI Image Generation.json) |
| Generate SEO Seed Keywords Using AI | generate | n8n-nodes-langchain.lmchatanthropic, n8n-nodes-langchain.agent, manual | 🔴 High | [Generate SEO Seed Keywords Using AI.json](workflows/Generate SEO Seed Keywords Using AI.json) |
| Generate SQL queries from schema only - AI-powered | generate | n8n-nodes-langchain.memorybufferwindow, n8n-nodes-langchain.chat, readwritefile | 🔴 High | [P307QnrxpA1ddsM5_Generate_SQL_queries_from_schema_only_-_AI-powered.json](workflows/P307QnrxpA1ddsM5_Generate_SQL_queries_from_schema_only_-_AI-powered.json) |
| Generate SQL queries from schema only - AI-powered | generate | n8n-nodes-langchain.memorybufferwindow, n8n-nodes-langchain.chat, readwritefile | 🔴 High | [Generate SQL queries from schema only - AI-powered.json](workflows/Generate SQL queries from schema only - AI-powered.json) |
| Generate audio from text using OpenAI - text-to-speech Workflow | generate | webhook, n8n-nodes-langchain.openai, respondtowebhook | 🟢 Low | [Generate audio from text using OpenAI and Webhook _ Text to Speech Workflow.json](workflows/Generate audio from text using OpenAI and Webhook _ Text to Speech Workflow.json) |
| Generate audio from text using OpenAI - text-to-speech Workflow | generate | webhook, n8n-nodes-langchain.openai, respondtowebhook | 🟢 Low | [OVSyGmI6YFviPu8Q_Generate_audio_from_text_using_OpenAI_-_text-to-speech_Workflow.json](workflows/OVSyGmI6YFviPu8Q_Generate_audio_from_text_using_OpenAI_-_text-to-speech_Workflow.json) |
| 🔍🛠️Generate SEO-Optimized WordPress Content with Perplexity Research | generate | wordpress, n8n-nodes-langchain.outputparserstructured, httprequest | 🔴 High | [5lMPjSDuoMvCJnko_🔍🛠️Generate_SEO-Optimized_WordPress_Content_with_Perplexity_Research.json](workflows/5lMPjSDuoMvCJnko_🔍🛠️Generate_SEO-Optimized_WordPress_Content_with_Perplexity_Research.json) |
| Monthly Spotify Track Archiving and Playlist Classification | monitor | n8n-nodes-langchain.chainllm, n8n-nodes-langchain.outputparserstructured, httprequest | 🔴 High | [Monthly Spotify Track Archiving and Playlist Classification.json](workflows/Monthly Spotify Track Archiving and Playlist Classification.json) |
| Automate SIEM Alert Enrichment with MITRE ATT&CK, Qdrant & Zendesk in n8n | notify | n8n-nodes-langchain.memorybufferwindow, splitinbatches, n8n-nodes-langchain.textsplittertokensplitter | 🔴 High | [Automate SIEM Alert Enrichment with MITRE ATT&CK, Qdrant & Zendesk in n8n.json](workflows/Automate SIEM Alert Enrichment with MITRE ATT&CK, Qdrant & Zendesk in n8n.json) |
| Error Alert and Summarizer | notify | error, n8n-nodes-langchain.outputparserstructured, gmail | 🔴 High | [3b1q6ZJTxeONrpUV_Error_Alert_and_Summarizer.json](workflows/3b1q6ZJTxeONrpUV_Error_Alert_and_Summarizer.json) |
| Colombian Invoices Processing | process | splitinbatches, googlesheets, n8n-nodes-langchain.calculator | 🔴 High | [Xs7x61YMFsbpB4vg_Colombian_Invoices_Processing.json](workflows/Xs7x61YMFsbpB4vg_Colombian_Invoices_Processing.json) |
| Convert YouTube Videos into SEO Blog Posts | process | gmail, httprequest, markdown | 🔴 High | [A0xnegTHL43LL3eP_Convert_YouTube_Videos_into_SEO_Blog_Posts.json](workflows/A0xnegTHL43LL3eP_Convert_YouTube_Videos_into_SEO_Blog_Posts.json) |
| Transform Image to Lego Style Using Line and Dall-E | process | webhook, httprequest, n8n-nodes-langchain.openai | 🟢 Low | [2738_Transform_Image_to_Lego_Style_Using_Line_and_Dall-E.json](workflows/2738_Transform_Image_to_Lego_Style_Using_Line_and_Dall-E.json) |
| Transform Image to Lego Style Using Line and Dall-E | process | webhook, httprequest, n8n-nodes-langchain.openai | 🟢 Low | [Transform Image to Lego Style Using Line and Dall-E.json](workflows/Transform Image to Lego Style Using Line and Dall-E.json) |
| Convert URL HTML to Markdown Format and Get Page Links | read | splitinbatches, httprequest, manual | 🔴 High | [Convert URL HTML to Markdown Format and Get Page Links.json](workflows/Convert URL HTML to Markdown Format and Get Page Links.json) |
| Learn Anything from HN - Get Top Resource Recommendations from Hacker News | read | n8n-nodes-langchain.chainllm, emailsend, httprequest | 🟡 Medium | [Learn Anything from HN - Get Top Resource Recommendations from Hacker News.json](workflows/Learn Anything from HN - Get Top Resource Recommendations from Hacker News.json) |
| Google Analytics: Weekly Report | report | n8n-nodes-langchain.calculator, emailsend, googleanalytics | 🔴 High | [Create a Google Analytics Data Report with AI and sent it to E-Mail and Telegram.json](workflows/Create a Google Analytics Data Report with AI and sent it to E-Mail and Telegram.json) |
| High-Level Service Page SEO Blueprint Report | report | splitinbatches, n8n-nodes-langchain.chainllm, httprequest | 🔴 High | [WETMyIJCbD3et6Rh_High-Level_Service_Page_SEO_Blueprint_Report.json](workflows/WETMyIJCbD3et6Rh_High-Level_Service_Page_SEO_Blueprint_Report.json) |
| Online Marketing Weekly Report | report | n8n-nodes-langchain.calculator, emailsend, googleanalytics | 🔴 High | [knmxcsujuHmViJl4_Online_Marketing_Weekly_Report.json](workflows/knmxcsujuHmViJl4_Online_Marketing_Weekly_Report.json) |
| RAG Workflow For Stock Earnings Report Analysis | report | splitinbatches, n8n-nodes-langchain.vectorstore, googledocs | 🔴 High | [fqaNojXWrspqjfkY_RAG_Workflow_For_Stock_Earnings_Report_Analysis.json](workflows/fqaNojXWrspqjfkY_RAG_Workflow_For_Stock_Earnings_Report_Analysis.json) |
| RAG Workflow For Stock Earnings Report Analysis | report | splitinbatches, n8n-nodes-langchain.vectorstore, googledocs | 🔴 High | [AI-Powered RAG Workflow For Stock Earnings Report Analysis.json](workflows/AI-Powered RAG Workflow For Stock Earnings Report Analysis.json) |
| UTM Link Creator & QR Code Generator with Scheduled Google Analytics Reports | report | n8n-nodes-langchain.memorybufferwindow, gmail, googleanalytics | 🔴 High | [SJrqDqTBIAyaZQkq_UTM_Link_Creator_&_QR_Code_Generator_with_Scheduled_Google_Analytics_Reports.json](workflows/SJrqDqTBIAyaZQkq_UTM_Link_Creator_&_QR_Code_Generator_with_Scheduled_Google_Analytics_Reports.json) |
| UTM Link Creator & QR Code Generator with Scheduled Google Analytics Reports | report | n8n-nodes-langchain.memorybufferwindow, gmail, googleanalytics | 🔴 High | [UTM Link Creator & QR Code Generator with Scheduled Google Analytics Reports.json](workflows/UTM Link Creator & QR Code Generator with Scheduled Google Analytics Reports.json) |
| Printify Automation - Update Title and Description - AlexK1919 | update | splitinbatches, n8n-nodes-langchain.calculator, httprequest | 🔴 High | [Optimize & Update Printify Title and Description Workflow.json](workflows/Optimize & Update Printify Title and Description Workflow.json) |
| Printify Automation - Update Title and Description - AlexK1919 | update | splitinbatches, n8n-nodes-langchain.calculator, httprequest | 🔴 High | [1V1gcK6vyczRqdZC_Printify_Automation_-_Update_Title_and_Description_-_AlexK1919.json](workflows/1V1gcK6vyczRqdZC_Printify_Automation_-_Update_Title_and_Description_-_AlexK1919.json) |
| Detect hallucinations using specialised Ollama model bespoke-minicheck | validate | n8n-nodes-langchain.lmollama, n8n-nodes-langchain.chainllm, manual | 🔴 High | [Detect hallucinations using specialised Ollama model bespoke-minicheck.json](workflows/Detect hallucinations using specialised Ollama model bespoke-minicheck.json) |

## UTIL

*512 workflows in this category*

| Workflow Name | Business Function | Key Integrations | Complexity | File |
|---------------|-------------------|------------------|------------|------|
|  | automate | manual, wekan | 🟢 Low | [728_.json](workflows/728_.json) |
|  | automate | unleashedsoftware, manual | 🟢 Low | [641_.json](workflows/641_.json) |
|  | automate | sse | 🟢 Low | [639_.json](workflows/639_.json) |
| 1001_workflow_1001 | automate | bitwarden | 🟢 Low | [1001_workflow_1001.json](workflows/1001_workflow_1001.json) |
| 1005_workflow_1005 | automate | plivo, openweathermap, cron | 🟢 Low | [1005_workflow_1005.json](workflows/1005_workflow_1005.json) |
| 100_workflow_100 | automate | N/A | 🟢 Low | [100_workflow_100.json](workflows/100_workflow_100.json) |
| 101_workflow_101 | automate | writebinaryfile | 🟢 Low | [101_workflow_101.json](workflows/101_workflow_101.json) |
| 1021_workflow_1021 | automate | copper, manual | 🟢 Low | [1021_workflow_1021.json](workflows/1021_workflow_1021.json) |
| 1028_workflow_1028 | automate | copper, manual | 🟢 Low | [1028_workflow_1028.json](workflows/1028_workflow_1028.json) |
| 1035_workflow_1035 | automate | googleslides, manual | 🟢 Low | [1035_workflow_1035.json](workflows/1035_workflow_1035.json) |
| 1047_workflow_1047 | automate | httprequest, awssqs, cron | 🟢 Low | [1047_workflow_1047.json](workflows/1047_workflow_1047.json) |
| 1048_workflow_1048 | automate | webflow, manual | 🟢 Low | [1048_workflow_1048.json](workflows/1048_workflow_1048.json) |
| 1049_workflow_1049 | automate | googlebigquery, httprequest, cron | 🟢 Low | [1049_workflow_1049.json](workflows/1049_workflow_1049.json) |
| 1068_workflow_1068 | automate | filemaker, manual | 🟢 Low | [1068_workflow_1068.json](workflows/1068_workflow_1068.json) |
| 1069_workflow_1069 | automate | mqtt, httprequest, cron | 🟢 Low | [1069_workflow_1069.json](workflows/1069_workflow_1069.json) |
| 1074_workflow_1074 | automate | nocodb, splitinbatches, schedule | 🔴 High | [1074_workflow_1074.json](workflows/1074_workflow_1074.json) |
| 1083_workflow_1083 | automate | emailsend, manual, ical | 🟢 Low | [1083_workflow_1083.json](workflows/1083_workflow_1083.json) |
| 1111_workflow_1111 | automate | awss3, manual, awstranscribe | 🟢 Low | [1111_workflow_1111.json](workflows/1111_workflow_1111.json) |
| 1112_workflow_1112 | automate | uptimerobot | 🟢 Low | [1112_workflow_1112.json](workflows/1112_workflow_1112.json) |
| 1114_workflow_1114 | automate | microsofttodo, manual | 🟢 Low | [1114_workflow_1114.json](workflows/1114_workflow_1114.json) |
| 1115_workflow_1115 | automate | git, manual | 🟢 Low | [1115_workflow_1115.json](workflows/1115_workflow_1115.json) |
| 1118_workflow_1118 | automate | splitinbatches, trello, googlecalendar | 🟡 Medium | [1118_workflow_1118.json](workflows/1118_workflow_1118.json) |
| 1150_workflow_1150 | automate | movebinarydata, httprequest, functionitem | 🟡 Medium | [1150_workflow_1150.json](workflows/1150_workflow_1150.json) |
| 1160_workflow_1160 | automate | splitinbatches, rssfeedread, manual | 🟡 Medium | [1160_workflow_1160.json](workflows/1160_workflow_1160.json) |
| 1169_workflow_1169 | automate | httprequest, manual | 🟡 Medium | [1169_workflow_1169.json](workflows/1169_workflow_1169.json) |
| 119_workflow_119 | automate | webhook, xml, respondtowebhook | 🟢 Low | [119_workflow_119.json](workflows/119_workflow_119.json) |
| 1243_workflow_1243 | automate | splitinbatches, n8ntrainingcustomerdatastore, httprequest | 🟡 Medium | [1243_workflow_1243.json](workflows/1243_workflow_1243.json) |
| 1250_workflow_1250 | automate | spreadsheetfile, itemlists, htmlextract | 🟡 Medium | [1250_workflow_1250.json](workflows/1250_workflow_1250.json) |
| 1254_workflow_1254 | automate | webhook, netlify | 🟢 Low | [1254_workflow_1254.json](workflows/1254_workflow_1254.json) |
| 1282_workflow_1282 | automate | awstextract, manual, awss3 | 🟢 Low | [1282_workflow_1282.json](workflows/1282_workflow_1282.json) |
| 1283_workflow_1283 | automate | emailsend, googledrive | 🟢 Low | [1283_workflow_1283.json](workflows/1283_workflow_1283.json) |
| 1306_workflow_1306 | automate | webhook, respondtowebhook | 🟢 Low | [1306_workflow_1306.json](workflows/1306_workflow_1306.json) |
| 1328_workflow_1328 | automate | manual | 🟢 Low | [1328_workflow_1328.json](workflows/1328_workflow_1328.json) |
| 1330_workflow_1330 | automate | httprequest, manual, n8ntrainingcustomerdatastore | 🟢 Low | [1330_workflow_1330.json](workflows/1330_workflow_1330.json) |
| 1338_workflow_1338 | automate | start, httprequest, manual | 🟢 Low | [1338_workflow_1338.json](workflows/1338_workflow_1338.json) |
| 1344_workflow_1344 | automate | nextcloud, emailreadimap | 🟢 Low | [1344_workflow_1344.json](workflows/1344_workflow_1344.json) |
| 1357_workflow_1357 | automate | editimage, itemlists, httprequest | 🟡 Medium | [1357_workflow_1357.json](workflows/1357_workflow_1357.json) |
| 1377_workflow_1377 | automate | manual | 🟢 Low | [1377_workflow_1377.json](workflows/1377_workflow_1377.json) |
| 1396_workflow_1396 | automate | awss3, googledrive | 🟢 Low | [1396_workflow_1396.json](workflows/1396_workflow_1396.json) |
| 13_workflow_13 | automate | httprequest, xml, dropbox | 🟢 Low | [13_workflow_13.json](workflows/13_workflow_13.json) |
| 1418_workflow_1418 | automate | itemlists, htmlextract, datetime | 🔴 High | [1418_workflow_1418.json](workflows/1418_workflow_1418.json) |
| 1435_workflow_1435 | automate | spreadsheetfile, respondtowebhook, webhook | 🟢 Low | [1435_workflow_1435.json](workflows/1435_workflow_1435.json) |
| 1440_workflow_1440 | automate | webhook, crypto | 🟢 Low | [1440_workflow_1440.json](workflows/1440_workflow_1440.json) |
| 1465_workflow_1465 | automate | datetime, emailsend, googlecalendar | 🔴 High | [1465_workflow_1465.json](workflows/1465_workflow_1465.json) |
| 1497_workflow_1497 | automate | manual | 🟢 Low | [1497_workflow_1497.json](workflows/1497_workflow_1497.json) |
| 1500_workflow_1500 | automate | manual | 🟢 Low | [1500_workflow_1500.json](workflows/1500_workflow_1500.json) |
| 1537_workflow_1537 | automate | functionitem, itemlists | 🟢 Low | [1537_workflow_1537.json](workflows/1537_workflow_1537.json) |
| 156_workflow_156 | automate | functionitem, executecommand | 🟢 Low | [156_workflow_156.json](workflows/156_workflow_156.json) |
| 1588_workflow_1588 | automate | webhook, respondtowebhook | 🟢 Low | [1588_workflow_1588.json](workflows/1588_workflow_1588.json) |
| 1621_workflow_1621 | automate | httprequest, manual, compression | 🟡 Medium | [1621_workflow_1621.json](workflows/1621_workflow_1621.json) |
| 1690_workflow_1690 | automate | itemlists, movebinarydata, emailsend | 🟡 Medium | [1690_workflow_1690.json](workflows/1690_workflow_1690.json) |
| 1692_workflow_1692 | automate | itemlists, movebinarydata, emailsend | 🟡 Medium | [1692_workflow_1692.json](workflows/1692_workflow_1692.json) |
| 1731_workflow_1731 | automate | spreadsheetfile, manual, writebinaryfile | 🟢 Low | [1731_workflow_1731.json](workflows/1731_workflow_1731.json) |
| 1744_workflow_1744 | automate | datetime, manual | 🟡 Medium | [1744_workflow_1744.json](workflows/1744_workflow_1744.json) |
| 1746_workflow_1746 | automate | n8ntrainingcustomerdatastore, manual | 🟡 Medium | [1746_workflow_1746.json](workflows/1746_workflow_1746.json) |
| 1747_workflow_1747 | automate | manual | 🔴 High | [1747_workflow_1747.json](workflows/1747_workflow_1747.json) |
| 1748_workflow_1748 | automate | itemlists, htmlextract, httprequest | 🔴 High | [1748_workflow_1748.json](workflows/1748_workflow_1748.json) |
| 1749_workflow_1749 | automate | splitinbatches, n8ntrainingcustomerdatastore, n8ntrainingcustomermessenger | 🔴 High | [1749_workflow_1749.json](workflows/1749_workflow_1749.json) |
| 1750_workflow_1750 | automate | webhook, respondtowebhook | 🟢 Low | [1750_workflow_1750.json](workflows/1750_workflow_1750.json) |
| 1790_workflow_1790 | automate | itemlists, n8ntrainingcustomerdatastore, emailsend | 🟡 Medium | [1790_workflow_1790.json](workflows/1790_workflow_1790.json) |
| 1799_workflow_1799 | automate | itemlists, htmlextract, httprequest | 🟡 Medium | [1799_workflow_1799.json](workflows/1799_workflow_1799.json) |
| 179_workflow_179 | automate | spreadsheetfile, typeform, nextcloud | 🟢 Low | [179_workflow_179.json](workflows/179_workflow_179.json) |
| 1821_workflow_1821 | automate | asana, webhook, zendesk | 🟡 Medium | [1821_workflow_1821.json](workflows/1821_workflow_1821.json) |
| 1823_workflow_1823 | automate | mondaycom, mautic | 🟢 Low | [1823_workflow_1823.json](workflows/1823_workflow_1823.json) |
| 1826_workflow_1826 | automate | spreadsheetfile, httprequest, ftp | 🔴 High | [1826_workflow_1826.json](workflows/1826_workflow_1826.json) |
| 1828_workflow_1828 | automate | mautic, calendly | 🟢 Low | [1828_workflow_1828.json](workflows/1828_workflow_1828.json) |
| 1833_workflow_1833 | automate | webhook, jira, zendesk | 🟡 Medium | [1833_workflow_1833.json](workflows/1833_workflow_1833.json) |
| 1892_workflow_1892 | automate | webhook, n8n, html | 🟡 Medium | [1892_workflow_1892.json](workflows/1892_workflow_1892.json) |
| 1913_workflow_1913 | automate | manual, n8ntrainingcustomerdatastore | 🟢 Low | [1913_workflow_1913.json](workflows/1913_workflow_1913.json) |
| 1914_workflow_1914 | automate | spreadsheetfile, microsoftsql, manual | 🟢 Low | [1914_workflow_1914.json](workflows/1914_workflow_1914.json) |
| 1916_workflow_1916 | automate | httprequest, manual | 🟢 Low | [1916_workflow_1916.json](workflows/1916_workflow_1916.json) |
| 1920_workflow_1920 | automate | webhook, httprequest, respondtowebhook | 🟢 Low | [1920_workflow_1920.json](workflows/1920_workflow_1920.json) |
| 1940_workflow_1940 | automate | httprequest, schedule, googlecalendar | 🟡 Medium | [1940_workflow_1940.json](workflows/1940_workflow_1940.json) |
| 1943_workflow_1943 | automate | comparedatasets, manual | 🟢 Low | [1943_workflow_1943.json](workflows/1943_workflow_1943.json) |
| 1994_workflow_1994 | automate | splitinbatches, stopanderror, webhook | 🔴 High | [1994_workflow_1994.json](workflows/1994_workflow_1994.json) |
| 2. Refresh Pipedrive tokens | automate | supabase, httprequest, stopanderror | 🔴 High | [IYgbtNpyB4E6Jbxo_2._Refresh_Pipedrive_tokens.json](workflows/IYgbtNpyB4E6Jbxo_2._Refresh_Pipedrive_tokens.json) |
| 2017_workflow_2017 | automate | webhook | 🟢 Low | [2017_workflow_2017.json](workflows/2017_workflow_2017.json) |
| 2027_workflow_2027 | automate | httprequest, graphql, webhook | 🔴 High | [2027_workflow_2027.json](workflows/2027_workflow_2027.json) |
| 2032_workflow_2032 | automate | httprequest, manual | 🟡 Medium | [2032_workflow_2032.json](workflows/2032_workflow_2032.json) |
| 2033_workflow_2033 | automate | httprequest, webhook, respondtowebhook | 🟡 Medium | [2033_workflow_2033.json](workflows/2033_workflow_2033.json) |
| 2042_workflow_2042 | automate | splitinbatches, manual, googledrive | 🟡 Medium | [2042_workflow_2042.json](workflows/2042_workflow_2042.json) |
| 2044_workflow_2044 | automate | schedule, spotify | 🟡 Medium | [2044_workflow_2044.json](workflows/2044_workflow_2044.json) |
| 2046_workflow_2046 | automate | httprequest, manual | 🔴 High | [2046_workflow_2046.json](workflows/2046_workflow_2046.json) |
| 2053_workflow_2053 | automate | httprequest, schedule | 🟡 Medium | [2053_workflow_2053.json](workflows/2053_workflow_2053.json) |
| 2062_workflow_2062 | automate | splitinbatches, itemlists, medium | 🟡 Medium | [2062_workflow_2062.json](workflows/2062_workflow_2062.json) |
| 2074_workflow_2074 | automate | datetime, mondaycom, error | 🟢 Low | [2074_workflow_2074.json](workflows/2074_workflow_2074.json) |
| 2075_workflow_2075 | automate | movebinarydata, datetime, schedule | 🔴 High | [2075_workflow_2075.json](workflows/2075_workflow_2075.json) |
| 2108_workflow_2108 | automate | httprequest, webhook, intercom | 🔴 High | [2108_workflow_2108.json](workflows/2108_workflow_2108.json) |
| 2123_workflow_2123 | automate | splitinbatches, httprequest, stopanderror | 🔴 High | [2123_workflow_2123.json](workflows/2123_workflow_2123.json) |
| 2133_workflow_2133 | automate | httprequest, webhook, xml | 🟡 Medium | [2133_workflow_2133.json](workflows/2133_workflow_2133.json) |
| 2134_workflow_2134 | automate | httprequest, webhook, removeduplicates | 🟡 Medium | [2134_workflow_2134.json](workflows/2134_workflow_2134.json) |
| 2147_workflow_2147 | automate | crypto, itemlists, datetime | 🔴 High | [2147_workflow_2147.json](workflows/2147_workflow_2147.json) |
| 2149_workflow_2149 | automate | schedule, todoist | 🟡 Medium | [2149_workflow_2149.json](workflows/2149_workflow_2149.json) |
| 2152_workflow_2152 | automate | respondtowebhook, httprequest, webhook | 🔴 High | [2152_workflow_2152.json](workflows/2152_workflow_2152.json) |
| 2153_workflow_2153 | automate | webhook, httprequest | 🟡 Medium | [2153_workflow_2153.json](workflows/2153_workflow_2153.json) |
| 2155_workflow_2155 | automate | httprequest, webhook, xml | 🟡 Medium | [2155_workflow_2155.json](workflows/2155_workflow_2155.json) |
| 216_workflow_216 | automate | webhook, graphql | 🟢 Low | [216_workflow_216.json](workflows/216_workflow_216.json) |
| 2171_workflow_2171 | automate | highlevel, httprequest, webhook | 🟡 Medium | [2171_workflow_2171.json](workflows/2171_workflow_2171.json) |
| 2179_workflow_2179 | automate | httprequest, manual, googledrive | 🔴 High | [2179_workflow_2179.json](workflows/2179_workflow_2179.json) |
| 2190_workflow_2190 | automate | clickup, webhook, respondtowebhook | 🟡 Medium | [2190_workflow_2190.json](workflows/2190_workflow_2190.json) |
| 2195_workflow_2195 | automate | httprequest, form, respondtowebhook | 🟡 Medium | [2195_workflow_2195.json](workflows/2195_workflow_2195.json) |
| 2214_workflow_2214 | automate | grist, webhook | 🟡 Medium | [2214_workflow_2214.json](workflows/2214_workflow_2214.json) |
| 2225_workflow_2225 | automate | httprequest, webhook | 🟡 Medium | [2225_workflow_2225.json](workflows/2225_workflow_2225.json) |
| 2239_workflow_2239 | automate | manual | 🟢 Low | [2239_workflow_2239.json](workflows/2239_workflow_2239.json) |
| 2244_workflow_2244 | automate | httprequest, webhook, respondtowebhook | 🟡 Medium | [2244_workflow_2244.json](workflows/2244_workflow_2244.json) |
| 2245_workflow_2245 | automate | httprequest, webhook, respondtowebhook | 🟡 Medium | [2245_workflow_2245.json](workflows/2245_workflow_2245.json) |
| 2251_workflow_2251 | automate | keap, httprequest, webhook | 🟡 Medium | [2251_workflow_2251.json](workflows/2251_workflow_2251.json) |
| 225_workflow_225 | automate | htmlextract, emailsend, httprequest | 🟡 Medium | [225_workflow_225.json](workflows/225_workflow_225.json) |
| 2270_workflow_2270 | automate | schedule, manual, executeworkflow | 🔴 High | [2270_workflow_2270.json](workflows/2270_workflow_2270.json) |
| 2274_workflow_2274 | automate | n8ntrainingcustomerdatastore, webhook, respondtowebhook | 🟡 Medium | [2274_workflow_2274.json](workflows/2274_workflow_2274.json) |
| 2280_workflow_2280 | automate | httprequest, manual, extractfromfile | 🟡 Medium | [2280_workflow_2280.json](workflows/2280_workflow_2280.json) |
| 2285_workflow_2285 | automate | splitinbatches, schedule, spotify | 🔴 High | [2285_workflow_2285.json](workflows/2285_workflow_2285.json) |
| 2291_workflow_2291 | automate | httprequest, sendinblue, executeworkflow | 🔴 High | [2291_workflow_2291.json](workflows/2291_workflow_2291.json) |
| 2294_workflow_2294 | automate | readwritefile, httprequest, manual | 🟢 Low | [2294_workflow_2294.json](workflows/2294_workflow_2294.json) |
| 2295_workflow_2295 | automate | manual, n8n, converttofile | 🟡 Medium | [2295_workflow_2295.json](workflows/2295_workflow_2295.json) |
| 2297_workflow_2297 | automate | httprequest, readwritefile, manual | 🟡 Medium | [2297_workflow_2297.json](workflows/2297_workflow_2297.json) |
| 2299_workflow_2299 | automate | schedule, httprequest | 🟢 Low | [2299_workflow_2299.json](workflows/2299_workflow_2299.json) |
| 2301_workflow_2301 | automate | httprequest, manual, n8n | 🔴 High | [2301_workflow_2301.json](workflows/2301_workflow_2301.json) |
| 2304_workflow_2304 | automate | readwritefile, httprequest, manual | 🟢 Low | [2304_workflow_2304.json](workflows/2304_workflow_2304.json) |
| 2305_workflow_2305 | automate | readwritefile, httprequest, manual | 🟢 Low | [2305_workflow_2305.json](workflows/2305_workflow_2305.json) |
| 2306_workflow_2306 | automate | httprequest, readwritefile, manual | 🟡 Medium | [2306_workflow_2306.json](workflows/2306_workflow_2306.json) |
| 2310_workflow_2310 | automate | readwritefile, httprequest, manual | 🟢 Low | [2310_workflow_2310.json](workflows/2310_workflow_2310.json) |
| 2314_workflow_2314 | automate | httprequest, readwritefile, manual | 🟡 Medium | [2314_workflow_2314.json](workflows/2314_workflow_2314.json) |
| 2316_workflow_2316 | automate | readwritefile, httprequest, manual | 🟢 Low | [2316_workflow_2316.json](workflows/2316_workflow_2316.json) |
| 2317_workflow_2317 | automate | readwritefile, httprequest, manual | 🟢 Low | [2317_workflow_2317.json](workflows/2317_workflow_2317.json) |
| 2331_workflow_2331 | automate | elasticsearch, httprequest, manual | 🔴 High | [2331_workflow_2331.json](workflows/2331_workflow_2331.json) |
| 2333_workflow_2333 | automate | executeworkflow, n8n-nodes-langchain.chat, httprequest | 🔴 High | [2333_workflow_2333.json](workflows/2333_workflow_2333.json) |
| 2334_workflow_2334 | automate | n8n-nodes-langchain.chainllm, n8n-nodes-langchain.outputparserstructured, n8n-nodes-langchain.lmchatmistralcloud | 🔴 High | [2334_workflow_2334.json](workflows/2334_workflow_2334.json) |
| 2335_workflow_2335 | automate | n8n-nodes-langchain.chainretrievalqa, n8n-nodes-langchain.chat, n8n-nodes-langchain.lmchatmistralcloud | 🔴 High | [2335_workflow_2335.json](workflows/2335_workflow_2335.json) |
| 2339_workflow_2339 | automate | n8n-nodes-langchain.chainretrievalqa, extractfromfile, converttofile | 🔴 High | [2339_workflow_2339.json](workflows/2339_workflow_2339.json) |
| 2349_workflow_2349 | automate | error, n8n | 🟢 Low | [2349_workflow_2349.json](workflows/2349_workflow_2349.json) |
| 2359_workflow_2359 | automate | httprequest | 🟡 Medium | [2359_workflow_2359.json](workflows/2359_workflow_2359.json) |
| 2368_workflow_2368 | automate | httprequest | 🟡 Medium | [2368_workflow_2368.json](workflows/2368_workflow_2368.json) |
| 2371_workflow_2371 | automate | schedule, ftp, mqtt | 🟡 Medium | [2371_workflow_2371.json](workflows/2371_workflow_2371.json) |
| 2380_workflow_2380 | automate | httprequest, webhook | 🟡 Medium | [2380_workflow_2380.json](workflows/2380_workflow_2380.json) |
| 2383_workflow_2383 | automate | httprequest, spotify, mqtt | 🔴 High | [2383_workflow_2383.json](workflows/2383_workflow_2383.json) |
| 2398_workflow_2398 | automate | httprequest, executeworkflow | 🟡 Medium | [2398_workflow_2398.json](workflows/2398_workflow_2398.json) |
| 2403_workflow_2403 | automate | datetime, httprequest, schedule | 🔴 High | [2403_workflow_2403.json](workflows/2403_workflow_2403.json) |
| 2417_workflow_2417 | automate | respondtowebhook, httprequest, form | 🔴 High | [2417_workflow_2417.json](workflows/2417_workflow_2417.json) |
| 2424_workflow_2424 | automate | httprequest, manual, dropbox | 🔴 High | [2424_workflow_2424.json](workflows/2424_workflow_2424.json) |
| 2443_workflow_2443 | automate | httprequest, schedule | 🔴 High | [2443_workflow_2443.json](workflows/2443_workflow_2443.json) |
| 2444_workflow_2444 | automate | httprequest, manual | 🔴 High | [2444_workflow_2444.json](workflows/2444_workflow_2444.json) |
| 2448_workflow_2448 | automate | httprequest, webhook, html | 🟡 Medium | [2448_workflow_2448.json](workflows/2448_workflow_2448.json) |
| 2450_workflow_2450 | automate | httprequest, stopanderror, schedule | 🔴 High | [2450_workflow_2450.json](workflows/2450_workflow_2450.json) |
| 2451_workflow_2451 | automate | manual, compression, awss3 | 🟡 Medium | [2451_workflow_2451.json](workflows/2451_workflow_2451.json) |
| 2459_workflow_2459 | automate | httprequest, manual, editimage | 🔴 High | [2459_workflow_2459.json](workflows/2459_workflow_2459.json) |
| 2469_workflow_2469 | automate | splitinbatches, itemlists, schedule | 🔴 High | [2469_workflow_2469.json](workflows/2469_workflow_2469.json) |
| 2471_workflow_2471 | automate | httprequest, webhook, respondtowebhook | 🟡 Medium | [2471_workflow_2471.json](workflows/2471_workflow_2471.json) |
| 2475_workflow_2475 | automate | httprequest, manual | 🔴 High | [2475_workflow_2475.json](workflows/2475_workflow_2475.json) |
| 2476_workflow_2476 | automate | splitinbatches, httprequest, manual | 🔴 High | [2476_workflow_2476.json](workflows/2476_workflow_2476.json) |
| 2485_workflow_2485 | automate | cron, httprequest | 🔴 High | [2485_workflow_2485.json](workflows/2485_workflow_2485.json) |
| 2494_workflow_2494 | automate | httprequest, manual | 🟡 Medium | [2494_workflow_2494.json](workflows/2494_workflow_2494.json) |
| 2499_workflow_2499 | automate | filemaker, crypto, webhook | 🟡 Medium | [2499_workflow_2499.json](workflows/2499_workflow_2499.json) |
| 2500_workflow_2500 | automate | elasticsearch, httprequest, cron | 🟢 Low | [2500_workflow_2500.json](workflows/2500_workflow_2500.json) |
| 2501_workflow_2501 | automate | httprequest, manual, googledrive | 🔴 High | [2501_workflow_2501.json](workflows/2501_workflow_2501.json) |
| 2510_workflow_2510 | automate | httprequest, webhook, executeworkflow | 🔴 High | [2510_workflow_2510.json](workflows/2510_workflow_2510.json) |
| 2523_workflow_2523 | automate | splitinbatches, httprequest, schedule | 🟡 Medium | [2523_workflow_2523.json](workflows/2523_workflow_2523.json) |
| 2527_workflow_2527 | automate | schedule, httprequest | 🟢 Low | [2527_workflow_2527.json](workflows/2527_workflow_2527.json) |
| 2531_workflow_2531 | automate | splitinbatches, httprequest, schedule | 🔴 High | [2531_workflow_2531.json](workflows/2531_workflow_2531.json) |
| 2536_workflow_2536 | automate | splitinbatches, httprequest, webhook | 🔴 High | [2536_workflow_2536.json](workflows/2536_workflow_2536.json) |
| 2538_workflow_2538 | automate | httprequest, schedule, webhook | 🟡 Medium | [2538_workflow_2538.json](workflows/2538_workflow_2538.json) |
| 2547_workflow_2547 | automate | supabase, httprequest, webhook | 🔴 High | [2547_workflow_2547.json](workflows/2547_workflow_2547.json) |
| 2570_workflow_2570 | automate | splitinbatches, httprequest, schedule | 🔴 High | [2570_workflow_2570.json](workflows/2570_workflow_2570.json) |
| 2571_workflow_2571 | automate | datetime, httprequest, rssfeedread | 🟡 Medium | [2571_workflow_2571.json](workflows/2571_workflow_2571.json) |
| 2572_workflow_2572 | automate | httprequest, manual, extractfromfile | 🟡 Medium | [2572_workflow_2572.json](workflows/2572_workflow_2572.json) |
| 2586_workflow_2586 | automate | httprequest, schedule, manual | 🟡 Medium | [2586_workflow_2586.json](workflows/2586_workflow_2586.json) |
| 2590_workflow_2590 | automate | emailsend, httprequest, markdown | 🟡 Medium | [2590_workflow_2590.json](workflows/2590_workflow_2590.json) |
| 2620_workflow_2620 | automate | calendly | 🔴 High | [2620_workflow_2620.json](workflows/2620_workflow_2620.json) |
| 2621_workflow_2621 | automate | calendly | 🔴 High | [2621_workflow_2621.json](workflows/2621_workflow_2621.json) |
| 2646_workflow_2646 | automate | schedule, manual, n8n | 🟡 Medium | [2646_workflow_2646.json](workflows/2646_workflow_2646.json) |
| 2649_workflow_2649 | automate | httprequest, manual, editimage | 🟡 Medium | [2649_workflow_2649.json](workflows/2649_workflow_2649.json) |
| 2684_workflow_2684 | automate | graphql, manual | 🟡 Medium | [2684_workflow_2684.json](workflows/2684_workflow_2684.json) |
| 2727_workflow_2727 | automate | webhook, servicenow, respondtowebhook | 🟡 Medium | [2727_workflow_2727.json](workflows/2727_workflow_2727.json) |
| 2755_workflow_2755 | automate | jotform | 🔴 High | [2755_workflow_2755.json](workflows/2755_workflow_2755.json) |
| 2764_workflow_2764 | automate | httprequest, manual, extractfromfile | 🟡 Medium | [2764_workflow_2764.json](workflows/2764_workflow_2764.json) |
| 2769_workflow_2769 | automate | webhook | 🔴 High | [2769_workflow_2769.json](workflows/2769_workflow_2769.json) |
| 2774_workflow_2774 | automate | typeform | 🔴 High | [2774_workflow_2774.json](workflows/2774_workflow_2774.json) |
| 2824_workflow_2824 | automate | httprequest, manual | 🟢 Low | [2824_workflow_2824.json](workflows/2824_workflow_2824.json) |
| 2835_workflow_2835 | automate | ssh, emailsend, httprequest | 🔴 High | [2835_workflow_2835.json](workflows/2835_workflow_2835.json) |
| 2836_workflow_2836 | automate | httprequest, manual | 🟢 Low | [2836_workflow_2836.json](workflows/2836_workflow_2836.json) |
| 2857_workflow_2857 | automate | httprequest, webhook, manual | 🔴 High | [2857_workflow_2857.json](workflows/2857_workflow_2857.json) |
| 2858_workflow_2858 | automate | splitinbatches, httprequest, schedule | 🟡 Medium | [2858_workflow_2858.json](workflows/2858_workflow_2858.json) |
| 2886_workflow_2886 | automate | splitinbatches, schedule, manual | 🟡 Medium | [2886_workflow_2886.json](workflows/2886_workflow_2886.json) |
| 2925_workflow_2925 | automate | ssh, emailsend, schedule | 🟡 Medium | [2925_workflow_2925.json](workflows/2925_workflow_2925.json) |
| 2951_workflow_2951 | automate | ssh, emailsend, schedule | 🟡 Medium | [2951_workflow_2951.json](workflows/2951_workflow_2951.json) |
| 2979_workflow_2979 | automate | googledrive, form | 🟡 Medium | [2979_workflow_2979.json](workflows/2979_workflow_2979.json) |
| 3054_workflow_3054 | automate | httprequest, manual | 🟡 Medium | [3054_workflow_3054.json](workflows/3054_workflow_3054.json) |
| 3102_workflow_3102 | automate | httprequest, manual, googledrive | 🔴 High | [3102_workflow_3102.json](workflows/3102_workflow_3102.json) |
| 3105_workflow_3105 | automate | readwritefile, httprequest, manual | 🟢 Low | [3105_workflow_3105.json](workflows/3105_workflow_3105.json) |
| 3112_workflow_3112 | automate | schedule, googledrive, n8n | 🟡 Medium | [3112_workflow_3112.json](workflows/3112_workflow_3112.json) |
| 3145_workflow_3145 | automate | httprequest, googledrive, form | 🟡 Medium | [3145_workflow_3145.json](workflows/3145_workflow_3145.json) |
| 3186_workflow_3186 | automate | stopanderror, webhook | 🔴 High | [3186_workflow_3186.json](workflows/3186_workflow_3186.json) |
| 3205_workflow_3205 | automate | httprequest, schedule, readwritefile | 🔴 High | [3205_workflow_3205.json](workflows/3205_workflow_3205.json) |
| 3281_workflow_3281 | automate | httprequest, readwritefile, manual | 🟡 Medium | [3281_workflow_3281.json](workflows/3281_workflow_3281.json) |
| 3293_workflow_3293 | automate | executecommand, schedule, n8n | 🟡 Medium | [3293_workflow_3293.json](workflows/3293_workflow_3293.json) |
| 3297_workflow_3297 | automate | nocodb, webhook, dropbox | 🔴 High | [3297_workflow_3297.json](workflows/3297_workflow_3297.json) |
| 3327_workflow_3327 | automate | splitinbatches, httprequest, schedule | 🟡 Medium | [3327_workflow_3327.json](workflows/3327_workflow_3327.json) |
| 3331_workflow_3331 | automate | webhook, respondtowebhook | 🟢 Low | [3331_workflow_3331.json](workflows/3331_workflow_3331.json) |
| 3333_workflow_3333 | automate | webhook, respondtowebhook | 🟢 Low | [3333_workflow_3333.json](workflows/3333_workflow_3333.json) |
| 3400_workflow_3400 | automate | httprequest, manual, executeworkflow | 🟡 Medium | [3400_workflow_3400.json](workflows/3400_workflow_3400.json) |
| 3409_workflow_3409 | automate | n8n-nodes-langchain.memorybufferwindow, executiondata, httprequest | 🔴 High | [3409_workflow_3409.json](workflows/3409_workflow_3409.json) |
| 3444_workflow_3444 | automate | webhook, redis | 🔴 High | [3444_workflow_3444.json](workflows/3444_workflow_3444.json) |
| 3445_workflow_3445 | automate | splitinbatches, httprequest, form | 🔴 High | [3445_workflow_3445.json](workflows/3445_workflow_3445.json) |
| 3512_workflow_3512 | automate | googledrive, googledrive | 🔴 High | [3512_workflow_3512.json](workflows/3512_workflow_3512.json) |
| 3547_workflow_3547 | automate | readbinaryfiles, manual, executecommand | 🟢 Low | [3547_workflow_3547.json](workflows/3547_workflow_3547.json) |
| 3578_workflow_3578 | automate | quickchart, manual, googledrive | 🟢 Low | [3578_workflow_3578.json](workflows/3578_workflow_3578.json) |
| 3630_workflow_3630 | automate | executecommand, executecommand, n8n-nodes-langchain.mcp | 🔴 High | [3630_workflow_3630.json](workflows/3630_workflow_3630.json) |
| 3632_workflow_3632 | automate | n8n-nodes-langchain.mcp, n8n-nodes-langchain.code, n8n-nodes-langchain.workflow | 🔴 High | [3632_workflow_3632.json](workflows/3632_workflow_3632.json) |
| 3637_workflow_3637 | automate | httprequest, n8n-nodes-langchain.mcp, n8n-nodes-langchain.workflow | 🔴 High | [3637_workflow_3637.json](workflows/3637_workflow_3637.json) |
| 3690_workflow_3690 | automate | httprequest, manual | 🟡 Medium | [3690_workflow_3690.json](workflows/3690_workflow_3690.json) |
| 3696_workflow_3696 | automate | converttofile, httprequest, manual | 🟡 Medium | [3696_workflow_3696.json](workflows/3696_workflow_3696.json) |
| 3697_workflow_3697 | automate | emailsend, httprequest, webhook | 🔴 High | [3697_workflow_3697.json](workflows/3697_workflow_3697.json) |
| 3709_workflow_3709 | automate | manual, googledrive, executeworkflow | 🔴 High | [3709_workflow_3709.json](workflows/3709_workflow_3709.json) |
| 3805_workflow_3805 | automate | webhook, respondtowebhook | 🟡 Medium | [3805_workflow_3805.json](workflows/3805_workflow_3805.json) |
| 3836_workflow_3836 | automate | splitinbatches, n8n-nodes-langchain.chat, httprequest | 🟡 Medium | [3836_workflow_3836.json](workflows/3836_workflow_3836.json) |
| 3869_workflow_3869 | automate | manual | 🟡 Medium | [3869_workflow_3869.json](workflows/3869_workflow_3869.json) |
| 3870_workflow_3870 | automate | manual | 🟡 Medium | [3870_workflow_3870.json](workflows/3870_workflow_3870.json) |
| 3913_workflow_3913 | automate | webhook, converttofile, respondtowebhook | 🟡 Medium | [3913_workflow_3913.json](workflows/3913_workflow_3913.json) |
| 3970_workflow_3970 | automate | webhook, respondtowebhook | 🔴 High | [3970_workflow_3970.json](workflows/3970_workflow_3970.json) |
| 3973_workflow_3973 | automate | webhook, respondtowebhook | 🟡 Medium | [3973_workflow_3973.json](workflows/3973_workflow_3973.json) |
| 3996_workflow_3996 | automate | n8n, manual | 🟢 Low | [3996_workflow_3996.json](workflows/3996_workflow_3996.json) |
| 3_workflow_3 | automate | httprequest, webhook, editimage | 🟢 Low | [3_workflow_3.json](workflows/3_workflow_3.json) |
| 418_workflow_418 | automate | medium, webhook, httprequest | 🟢 Low | [418_workflow_418.json](workflows/418_workflow_418.json) |
| 434_workflow_434 | automate | httprequest, manual, htmlextract | 🟢 Low | [434_workflow_434.json](workflows/434_workflow_434.json) |
| 435_workflow_435 | automate | httprequest | 🟢 Low | [435_workflow_435.json](workflows/435_workflow_435.json) |
| 437_workflow_437 | automate | httprequest, readbinaryfile | 🟢 Low | [437_workflow_437.json](workflows/437_workflow_437.json) |
| 441_workflow_441 | automate | signl4, manual | 🟢 Low | [441_workflow_441.json](workflows/441_workflow_441.json) |
| 448_workflow_448 | automate | freshdesk, manual | 🟢 Low | [448_workflow_448.json](workflows/448_workflow_448.json) |
| 467_workflow_467 | automate | mautic, webhook | 🔴 High | [467_workflow_467.json](workflows/467_workflow_467.json) |
| 501_workflow_501 | automate | awssns, manual | 🟢 Low | [501_workflow_501.json](workflows/501_workflow_501.json) |
| 507_workflow_507 | automate | awsses, manual | 🟢 Low | [507_workflow_507.json](workflows/507_workflow_507.json) |
| 509_workflow_509 | automate | awssns | 🟢 Low | [509_workflow_509.json](workflows/509_workflow_509.json) |
| 510_workflow_510 | automate | awslambda, manual | 🟢 Low | [510_workflow_510.json](workflows/510_workflow_510.json) |
| 515_workflow_515 | automate | writebinaryfile, manual, googledrive | 🟢 Low | [515_workflow_515.json](workflows/515_workflow_515.json) |
| 518_workflow_518 | automate | cockpit, manual | 🟢 Low | [518_workflow_518.json](workflows/518_workflow_518.json) |
| 519_workflow_519 | automate | hunter, manual | 🟢 Low | [519_workflow_519.json](workflows/519_workflow_519.json) |
| 520_workflow_520 | automate | mailjet, manual | 🟢 Low | [520_workflow_520.json](workflows/520_workflow_520.json) |
| 521_workflow_521 | automate | mailjet | 🟢 Low | [521_workflow_521.json](workflows/521_workflow_521.json) |
| 522_workflow_522 | automate | manual, mailgun | 🟢 Low | [522_workflow_522.json](workflows/522_workflow_522.json) |
| 525_workflow_525 | automate | manual, hackernews | 🟢 Low | [525_workflow_525.json](workflows/525_workflow_525.json) |
| 529_workflow_529 | automate | bitbucket | 🟢 Low | [529_workflow_529.json](workflows/529_workflow_529.json) |
| 533_workflow_533 | automate | acuityscheduling | 🟢 Low | [533_workflow_533.json](workflows/533_workflow_533.json) |
| 534_workflow_534 | automate | invoiceninja, manual | 🟢 Low | [534_workflow_534.json](workflows/534_workflow_534.json) |
| 535_workflow_535 | automate | invoiceninja | 🟢 Low | [535_workflow_535.json](workflows/535_workflow_535.json) |
| 536_workflow_536 | automate | clockify | 🟢 Low | [536_workflow_536.json](workflows/536_workflow_536.json) |
| 537_workflow_537 | automate | copper | 🟢 Low | [537_workflow_537.json](workflows/537_workflow_537.json) |
| 538_workflow_538 | automate | eventbrite | 🟢 Low | [538_workflow_538.json](workflows/538_workflow_538.json) |
| 539_workflow_539 | automate | rundeck, manual | 🟢 Low | [539_workflow_539.json](workflows/539_workflow_539.json) |
| 540_workflow_540 | automate | calendly | 🟢 Low | [540_workflow_540.json](workflows/540_workflow_540.json) |
| 541_workflow_541 | automate | jotform | 🟢 Low | [541_workflow_541.json](workflows/541_workflow_541.json) |
| 543_workflow_543 | automate | xero, manual | 🟢 Low | [543_workflow_543.json](workflows/543_workflow_543.json) |
| 544_workflow_544 | automate | bannerbear, manual | 🟢 Low | [544_workflow_544.json](workflows/544_workflow_544.json) |
| 545_workflow_545 | automate | bannerbear, manual | 🟢 Low | [545_workflow_545.json](workflows/545_workflow_545.json) |
| 549_workflow_549 | automate | mautic, manual | 🟢 Low | [549_workflow_549.json](workflows/549_workflow_549.json) |
| 551_workflow_551 | automate | surveymonkey | 🟢 Low | [551_workflow_551.json](workflows/551_workflow_551.json) |
| 553_workflow_553 | automate | keap, manual | 🟢 Low | [553_workflow_553.json](workflows/553_workflow_553.json) |
| 554_workflow_554 | automate | keap | 🟢 Low | [554_workflow_554.json](workflows/554_workflow_554.json) |
| 556_workflow_556 | automate | mondaycom, manual | 🟢 Low | [556_workflow_556.json](workflows/556_workflow_556.json) |
| 557_workflow_557 | automate | manual, redis | 🟢 Low | [557_workflow_557.json](workflows/557_workflow_557.json) |
| 558_workflow_558 | automate | graphql, manual | 🟢 Low | [558_workflow_558.json](workflows/558_workflow_558.json) |
| 559_workflow_559 | automate | box, manual | 🟢 Low | [559_workflow_559.json](workflows/559_workflow_559.json) |
| 560_workflow_560 | automate | box | 🟢 Low | [560_workflow_560.json](workflows/560_workflow_560.json) |
| 565_workflow_565 | automate | microsoftonedrive, manual | 🟢 Low | [565_workflow_565.json](workflows/565_workflow_565.json) |
| 566_workflow_566 | automate | manual, microsoftexcel | 🟢 Low | [566_workflow_566.json](workflows/566_workflow_566.json) |
| 567_workflow_567 | automate | manual, helpscout | 🟢 Low | [567_workflow_567.json](workflows/567_workflow_567.json) |
| 569_workflow_569 | automate | jira | 🟢 Low | [569_workflow_569.json](workflows/569_workflow_569.json) |
| 571_workflow_571 | automate | manual, mandrill | 🟢 Low | [571_workflow_571.json](workflows/571_workflow_571.json) |
| 574_workflow_574 | automate | crypto, manual | 🟢 Low | [574_workflow_574.json](workflows/574_workflow_574.json) |
| 575_workflow_575 | automate | datetime, manual | 🟢 Low | [575_workflow_575.json](workflows/575_workflow_575.json) |
| 576_workflow_576 | automate | httprequest, editimage, manual | 🟢 Low | [576_workflow_576.json](workflows/576_workflow_576.json) |
| 577_workflow_577 | automate | manual, readbinaryfile | 🟢 Low | [577_workflow_577.json](workflows/577_workflow_577.json) |
| 578_workflow_578 | automate | readbinaryfiles, manual | 🟢 Low | [578_workflow_578.json](workflows/578_workflow_578.json) |
| 581_workflow_581 | automate | manual | 🟢 Low | [581_workflow_581.json](workflows/581_workflow_581.json) |
| 582_workflow_582 | automate | renamekeys, manual | 🟢 Low | [582_workflow_582.json](workflows/582_workflow_582.json) |
| 583_workflow_583 | automate | rssfeedread, manual | 🟢 Low | [583_workflow_583.json](workflows/583_workflow_583.json) |
| 584_workflow_584 | automate | emailsend, manual | 🟢 Low | [584_workflow_584.json](workflows/584_workflow_584.json) |
| 585_workflow_585 | automate | manual, readpdf, readbinaryfile | 🟢 Low | [585_workflow_585.json](workflows/585_workflow_585.json) |
| 586_workflow_586 | automate | spreadsheetfile, manual, readbinaryfile | 🟢 Low | [586_workflow_586.json](workflows/586_workflow_586.json) |
| 587_workflow_587 | automate | emailreadimap | 🟢 Low | [587_workflow_587.json](workflows/587_workflow_587.json) |
| 588_workflow_588 | automate | manual, executeworkflow | 🟢 Low | [588_workflow_588.json](workflows/588_workflow_588.json) |
| 597_workflow_597 | automate | manual, cratedb | 🟢 Low | [597_workflow_597.json](workflows/597_workflow_597.json) |
| 602_workflow_602 | automate | httprequest, manual | 🟢 Low | [602_workflow_602.json](workflows/602_workflow_602.json) |
| 615_workflow_615 | automate | httprequest, dropbox, manual | 🟢 Low | [615_workflow_615.json](workflows/615_workflow_615.json) |
| 620_workflow_620 | automate | nextcloud, httprequest, manual | 🟢 Low | [620_workflow_620.json](workflows/620_workflow_620.json) |
| 655_workflow_655 | automate | manual | 🟢 Low | [655_workflow_655.json](workflows/655_workflow_655.json) |
| 663_workflow_663 | automate | ftp, httprequest, manual | 🟢 Low | [663_workflow_663.json](workflows/663_workflow_663.json) |
| 688_workflow_688 | automate | manual | 🟡 Medium | [688_workflow_688.json](workflows/688_workflow_688.json) |
| 695_workflow_695 | automate | manual | 🟢 Low | [695_workflow_695.json](workflows/695_workflow_695.json) |
| 737_workflow_737 | automate | webhook, openweathermap | 🟢 Low | [737_workflow_737.json](workflows/737_workflow_737.json) |
| 763_workflow_763 | automate | N/A | 🟢 Low | [763_workflow_763.json](workflows/763_workflow_763.json) |
| 766_workflow_766 | automate | N/A | 🟢 Low | [766_workflow_766.json](workflows/766_workflow_766.json) |
| 767_workflow_767 | automate | N/A | 🟢 Low | [767_workflow_767.json](workflows/767_workflow_767.json) |
| 837_workflow_837 | automate | htmlextract, emailsend, httprequest | 🔴 High | [837_workflow_837.json](workflows/837_workflow_837.json) |
| 880_workflow_880 | automate | httprequest, cron | 🟢 Low | [880_workflow_880.json](workflows/880_workflow_880.json) |
| 890_workflow_890 | automate | spreadsheetfile, manual, readbinaryfile | 🟢 Low | [890_workflow_890.json](workflows/890_workflow_890.json) |
| 8_workflow_8 | automate | error, mailgun | 🟢 Low | [8_workflow_8.json](workflows/8_workflow_8.json) |
| 908_workflow_908 | automate | httprequest, compression, dropbox | 🟢 Low | [908_workflow_908.json](workflows/908_workflow_908.json) |
| 913_workflow_913 | automate | movebinarydata, executecommand, manual | 🟡 Medium | [913_workflow_913.json](workflows/913_workflow_913.json) |
| 917_workflow_917 | automate | httprequest, timescaledb, cron | 🟢 Low | [917_workflow_917.json](workflows/917_workflow_917.json) |
| 920_workflow_920 | automate | manual, securityscorecard | 🟢 Low | [920_workflow_920.json](workflows/920_workflow_920.json) |
| 928_workflow_928 | automate | manual, reddit | 🟢 Low | [928_workflow_928.json](workflows/928_workflow_928.json) |
| 930_workflow_930 | automate | manual, discourse | 🟢 Low | [930_workflow_930.json](workflows/930_workflow_930.json) |
| 934_workflow_934 | automate | stackby, manual | 🟢 Low | [934_workflow_934.json](workflows/934_workflow_934.json) |
| 935_workflow_935 | automate | manual, peekalink | 🟢 Low | [935_workflow_935.json](workflows/935_workflow_935.json) |
| 936_workflow_936 | automate | tapfiliate, manual | 🟢 Low | [936_workflow_936.json](workflows/936_workflow_936.json) |
| 947_workflow_947 | automate | typeform, demio | 🟢 Low | [947_workflow_947.json](workflows/947_workflow_947.json) |
| 949_workflow_949 | automate | quickbooks | 🟢 Low | [949_workflow_949.json](workflows/949_workflow_949.json) |
| 959_workflow_959 | automate | raindrop | 🟢 Low | [959_workflow_959.json](workflows/959_workflow_959.json) |
| 960_workflow_960 | automate | gotowebinar | 🟢 Low | [960_workflow_960.json](workflows/960_workflow_960.json) |
| 961_workflow_961 | automate | emelia | 🟢 Low | [961_workflow_961.json](workflows/961_workflow_961.json) |
| 966_workflow_966 | automate | schedule, openweathermap, manual | 🟢 Low | [966_workflow_966.json](workflows/966_workflow_966.json) |
| 968_workflow_968 | automate | webhook, posthog | 🟢 Low | [968_workflow_968.json](workflows/968_workflow_968.json) |
| 986_workflow_986 | automate | openweathermap, webhook | 🟢 Low | [986_workflow_986.json](workflows/986_workflow_986.json) |
| 987_workflow_987 | automate | webhook, asana | 🟢 Low | [987_workflow_987.json](workflows/987_workflow_987.json) |
| 989_workflow_989 | automate | typeform, apitemplateio | 🟢 Low | [989_workflow_989.json](workflows/989_workflow_989.json) |
| 990_workflow_990 | automate | autopilot | 🟢 Low | [990_workflow_990.json](workflows/990_workflow_990.json) |
| 992_workflow_992 | automate | wise | 🟢 Low | [992_workflow_992.json](workflows/992_workflow_992.json) |
| 995_workflow_995 | automate | splitinbatches, manual | 🟢 Low | [995_workflow_995.json](workflows/995_workflow_995.json) |
| 996_workflow_996 | automate | splitinbatches, manual | 🟢 Low | [996_workflow_996.json](workflows/996_workflow_996.json) |
| 998_workflow_998 | automate | deepl, httprequest | 🟢 Low | [998_workflow_998.json](workflows/998_workflow_998.json) |
| A workflow with the Twilio node | automate | manual, twilio | 🟢 Low | [401_A_workflow_with_the_Twilio_node.json](workflows/401_A_workflow_with_the_Twilio_node.json) |
| ALL_unique_nodes | automate | N/A | 🟢 Low | [ALL_unique_nodes.json](workflows/ALL_unique_nodes.json) |
| Activity Encouragement | automate | strava, emailsend, cron | 🟡 Medium | [14_Activity_Encouragement.json](workflows/14_Activity_Encouragement.json) |
| Assign values to variables using the Set node | automate | manual | 🟢 Low | [141_Assign_values_to_variables_using_the_Set_node.json](workflows/141_Assign_values_to_variables_using_the_Set_node.json) |
| Auth0 User Login | automate | httprequest, stopanderror, webhook | 🔴 High | [AS2Rj41p6OyA0xZK_Auth0_User_Login.json](workflows/AS2Rj41p6OyA0xZK_Auth0_User_Login.json) |
| Auto - Resume Disabled Workflows | automate | schedule, n8n, manual | 🟢 Low | [kZarev2IMUaKHhCI_Auto_-_Resume_Disabled_Workflows.json](workflows/kZarev2IMUaKHhCI_Auto_-_Resume_Disabled_Workflows.json) |
| Basic PDF Digital Sign Service | automate | readwritefile, webhook, converttofile | 🔴 High | [V1vbO2m79cFNH59h_Basic_PDF_Digital_Sign_Service.json](workflows/V1vbO2m79cFNH59h_Basic_PDF_Digital_Sign_Service.json) |
| Calculate the Centroid of a Set of Vectors | automate | webhook, respondtowebhook | 🟡 Medium | [g3q68zSOQvTcydLs_Calculate_the_Centroid_of_a_Set_of_Vectors.json](workflows/g3q68zSOQvTcydLs_Calculate_the_Centroid_of_a_Set_of_Vectors.json) |
| Chinese Translator | automate | httprequest, webhook, extractfromfile | 🔴 High | [iFkGAiVn3yBlykIG_Chinese_Translator.json](workflows/iFkGAiVn3yBlykIG_Chinese_Translator.json) |
| Clone n8n Workflows between Instances using n8n API | automate | splitinbatches, httprequest, manual | 🔴 High | [yOhH9SGiZgZTDUB4_Clone_n8n_Workflows_between_Instances_using_n8n_API.json](workflows/yOhH9SGiZgZTDUB4_Clone_n8n_Workflows_between_Instances_using_n8n_API.json) |
| Coffee Bot (Matrix) | automate | matrix, cron | 🟢 Low | [9_Coffee_Bot_(Matrix).json](workflows/9_Coffee_Bot_(Matrix).json) |
| Complete Guide to Setting Up and Generating TOTP Codes in n8n 🔐 | automate | manual, totp | 🟢 Low | [0wfomsVO0TQtQkwU_Complete_Guide_to_Setting_Up_and_Generating_TOTP_Codes_in_n8n_🔐.json](workflows/0wfomsVO0TQtQkwU_Complete_Guide_to_Setting_Up_and_Generating_TOTP_Codes_in_n8n_🔐.json) |
| Creating a meeting with the Zoom node | automate | zoom, manual | 🟢 Low | [83_Creating_a_meeting_with_the_Zoom_node.json](workflows/83_Creating_a_meeting_with_the_Zoom_node.json) |
| Creating your first workflow | automate | openweathermap, cron, twilio | 🟢 Low | [69_Creating_your_first_workflow.json](workflows/69_Creating_your_first_workflow.json) |
| DigialOceanUpload | automate | form, form | 🟢 Low | [CYv2u2izrgZWk5bK_DigialOceanUpload.json](workflows/CYv2u2izrgZWk5bK_DigialOceanUpload.json) |
| Dynamic credentials using expressions | automate | respondtowebhook, nasa, form | 🟡 Medium | [2223_Dynamic_credentials_using_expressions.json](workflows/2223_Dynamic_credentials_using_expressions.json) |
| Enhance Security Operations with the Qualys Slack Shortcut Bot! | automate | httprequest, webhook, executeworkflow | 🔴 High | [Enhance Security Operations with the Qualys Slack Shortcut Bot!.json](workflows/Enhance Security Operations with the Qualys Slack Shortcut Bot!.json) |
| Enhance Security Operations with the Qualys Slack Shortcut Bot! (1) | automate | httprequest, webhook, executeworkflow | 🔴 High | [Enhance Security Operations with the Qualys Slack Shortcut Bot! (1).json](workflows/Enhance Security Operations with the Qualys Slack Shortcut Bot! (1).json) |
| Execute a command that gives the hard disk memory used on the host machine | automate | executecommand, cron, twilio | 🟢 Low | [81_Execute_a_command_that_gives_the_hard_disk_memory_used_on_the_host_machine.json](workflows/81_Execute_a_command_that_gives_the_hard_disk_memory_used_on_the_host_machine.json) |
| Execute an SQL query in Microsoft SQL | automate | microsoftsql, manual | 🟢 Low | [99_Execute_an_SQL_query_in_Microsoft_SQL.json](workflows/99_Execute_an_SQL_query_in_Microsoft_SQL.json) |
| FLUX-fill standalone | automate | httprequest, webhook, html | 🔴 High | [🎨 Interactive Image Editor with FLUX.1 Fill Tool for Inpainting.json](workflows/🎨 Interactive Image Editor with FLUX.1 Fill Tool for Inpainting.json) |
| FLUX-fill standalone | automate | httprequest, webhook, html | 🔴 High | [OvuZIXwt9mdU2JGK_FLUX-fill_standalone.json](workflows/OvuZIXwt9mdU2JGK_FLUX-fill_standalone.json) |
| Find Top Keywords | automate | splitinbatches, nocodb, httprequest | 🔴 High | [SHgOqN3ednIo5gNu_Find_Top_Keywords.json](workflows/SHgOqN3ednIo5gNu_Find_Top_Keywords.json) |
| Find a New Book | automate | emailsend, httprequest, manual | 🟡 Medium | [12_Find_a_New_Book.json](workflows/12_Find_a_New_Book.json) |
| Format US Phone Number | automate | executeworkflow | 🟡 Medium | [mNbQmMNEvpiZqASG_Format_US_Phone_Number.json](workflows/mNbQmMNEvpiZqASG_Format_US_Phone_Number.json) |
| General 3D Presentation | automate | httprequest, manual | 🔴 High | [vpZ1wpsniCvKYjCF_General_3D_Presentation.json](workflows/vpZ1wpsniCvKYjCF_General_3D_Presentation.json) |
| Google Cal to Zoom meeting | automate | datetime, googlecalendar, manual | 🟡 Medium | [1_Google_Cal_to_Zoom_meeting.json](workflows/1_Google_Cal_to_Zoom_meeting.json) |
| Image to license plate number | automate | n8n-nodes-langchain.chainllm, form, n8n-nodes-langchain.lmchatopenrouter | 🟢 Low | [Extract license plate number from image uploaded via an n8n form.json](workflows/Extract license plate number from image uploaded via an n8n form.json) |
| Image to license plate number | automate | n8n-nodes-langchain.chainllm, form, n8n-nodes-langchain.lmchatopenrouter | 🟢 Low | [B37wvB0tdKgjuabw_Image_to_license_plate_number.json](workflows/B37wvB0tdKgjuabw_Image_to_license_plate_number.json) |
| KB Tool - Confluence Knowledge Base | automate | httprequest, executeworkflow | 🟡 Medium | [KB Tool - Confluence Knowledge Base.json](workflows/KB Tool - Confluence Knowledge Base.json) |
| MCP_CALENDAR | automate | n8n-nodes-langchain.mcp, googlecalendar | 🟢 Low | [grxwlyzZb3z4WLAa_MCP_CALENDAR.json](workflows/grxwlyzZb3z4WLAa_MCP_CALENDAR.json) |
| Manipulate PDF with Adobe developer API | automate | httprequest, manual, dropbox | 🔴 High | [Manipulate PDF with Adobe developer API.json](workflows/Manipulate PDF with Adobe developer API.json) |
| Merge | automate | readwritefile, httprequest, manual | 🟢 Low | [do4h6jnTGWDjCXV7_Merge.json](workflows/do4h6jnTGWDjCXV7_Merge.json) |
| Merge PDFs | automate | readwritefile, httprequest, manual | 🟡 Medium | [MVPlLz3CiQok6rXy_Merge_PDFs.json](workflows/MVPlLz3CiQok6rXy_Merge_PDFs.json) |
| Merge multiple runs into one | automate | splitinbatches, n8ntrainingcustomerdatastore, manual | 🟡 Medium | [ynTqojfUnGpG2rBP_Merge_multiple_runs_into_one.json](workflows/ynTqojfUnGpG2rBP_Merge_multiple_runs_into_one.json) |
| Multi-Agent Conversation | automate | splitinbatches, n8n-nodes-langchain.memorybufferwindow, n8n-nodes-langchain.chat | 🔴 High | [0QQxgdQABUbbDJ0G_Multi-Agent_Conversation.json](workflows/0QQxgdQABUbbDJ0G_Multi-Agent_Conversation.json) |
| My workflow | automate | spreadsheetfile, splitinbatches, emailsend | 🟡 Medium | [1_My_workflow.json](workflows/1_My_workflow.json) |
| My workflow | automate | n8n-nodes-langchain.chainllm, n8n-nodes-langchain.outputparserstructured, n8n-nodes-langchain.lmchatopenrouter | 🟡 Medium | [eHuvG2I1vOYj0U6k_My_workflow.json](workflows/eHuvG2I1vOYj0U6k_My_workflow.json) |
| My workflow 2 | automate | httprequest, schedule | 🔴 High | [3081_My_workflow_2.json](workflows/3081_My_workflow_2.json) |
| My workflow 6 | automate | httprequest, manual | 🟢 Low | [rLoXUoKSZ4a9XUAv_My_workflow_6.json](workflows/rLoXUoKSZ4a9XUAv_My_workflow_6.json) |
| N8N Español - Ejemplos | automate | manual, executecommand | 🟡 Medium | [29_N8N_Español_-_Ejemplos.json](workflows/29_N8N_Español_-_Ejemplos.json) |
| NameCheap Dynamic DNS (DDNS) | automate | httprequest, cron | 🟡 Medium | [3_NameCheap_Dynamic_DNS_(DDNS).json](workflows/3_NameCheap_Dynamic_DNS_(DDNS).json) |
| NetSuite Rest API workflow | automate | webhook, manual | 🟢 Low | [FDl4Ho3KYiA7MIxR_NetSuite_Rest_API_workflow.json](workflows/FDl4Ho3KYiA7MIxR_NetSuite_Rest_API_workflow.json) |
| OIDC client workflow | automate | httprequest, webhook, html | 🔴 High | [zeyTmqqmXaQIFWzV_OIDC_client_workflow.json](workflows/zeyTmqqmXaQIFWzV_OIDC_client_workflow.json) |
| Optimise images uploaded to GDrive | automate | httprequest, googledrive, googledrive | 🟡 Medium | [FpZJ8jaNQ3j2DO1L_Optimise_images_uploaded_to_GDrive.json](workflows/FpZJ8jaNQ3j2DO1L_Optimise_images_uploaded_to_GDrive.json) |
| Perplexity Researcher | automate | httprequest, executeworkflow | 🟢 Low | [5uapJIjLLhwnhX0n_Perplexity_Researcher.json](workflows/5uapJIjLLhwnhX0n_Perplexity_Researcher.json) |
| Plex Automatic Throttler | automate | httprequest, webhook | 🔴 High | [11_Plex_Automatic_Throttler.json](workflows/11_Plex_Automatic_Throttler.json) |
| Prevent concurrent workflow runs using Redis | automate | redis, stopanderror, manual | 🔴 High | [3976_Prevent_concurrent_workflow_runs_using_Redis.json](workflows/3976_Prevent_concurrent_workflow_runs_using_Redis.json) |
| Push Multiple Files to Github Repo via Github REST API | automate | httprequest, manual | 🟡 Medium | [RtTHLr1SAwIpntKr_Push_Multiple_Files_to_Github_Repo_via_Github_REST_API.json](workflows/RtTHLr1SAwIpntKr_Push_Multiple_Files_to_Github_Repo_via_Github_REST_API.json) |
| Query List of Sign-in IPs | automate | movebinarydata, httprequest, converttofile | 🔴 High | [fGq0vUaD6JoqAbDa_Query_List_of_Sign-in_IPs.json](workflows/fGq0vUaD6JoqAbDa_Query_List_of_Sign-in_IPs.json) |
| React to PDFMonkey Callback | automate | webhook, httprequest | 🟢 Low | [s6nTFZfg6xjWyJRX_React_to_PDFMonkey_Callback.json](workflows/s6nTFZfg6xjWyJRX_React_to_PDFMonkey_Callback.json) |
| Receive the weather information of any city | automate | openweathermap, webhook | 🟢 Low | [158_Receive_the_weather_information_of_any_city.json](workflows/158_Receive_the_weather_information_of_any_city.json) |
| Recipe Recommendations with Qdrant and Mistral | automate | N/A | 🟢 Low | [Recipe Recommendations with Qdrant and Mistral.json](workflows/Recipe Recommendations with Qdrant and Mistral.json) |
| Reschedule overdue Asana tasks and clean up completed tasks | automate | schedule, asana | 🟡 Medium | [RJ4PaYq0JBr29KJm_Reschedule_overdue_Asana_tasks_and_clean_up_completed_tasks.json](workflows/RJ4PaYq0JBr29KJm_Reschedule_overdue_Asana_tasks_and_clean_up_completed_tasks.json) |
| Retry Execution Hourly | automate | splitinbatches, httprequest, schedule | 🔴 High | [JJKkNnO4PQ12gQdE_Retry_Execution_Hourly.json](workflows/JJKkNnO4PQ12gQdE_Retry_Execution_Hourly.json) |
| Sample Spotify | automate | manual, spotify | 🟢 Low | [8_Sample_Spotify.json](workflows/8_Sample_Spotify.json) |
| Scans von PDF zu Nextcloud | automate | schedule, nextcloud, httprequest | 🟢 Low | [EJHT9UmGXNOyynV0_Scans_von_PDF_zu_Nextcloud.json](workflows/EJHT9UmGXNOyynV0_Scans_von_PDF_zu_Nextcloud.json) |
| Sell a Used Car | automate | airtop, manual | 🟡 Medium | [ViCY8FzVGcRsxVcK_Sell_a_Used_Car.json](workflows/ViCY8FzVGcRsxVcK_Sell_a_Used_Car.json) |
| Send TTS (Text-to-speech) voice calls | automate | httprequest, form | 🟢 Low | [GrGmuKzZAsCkd4bt_Send_TTS_(Text-to-speech)_voice_calls.json](workflows/GrGmuKzZAsCkd4bt_Send_TTS_(Text-to-speech)_voice_calls.json) |
| Send an SMS to a number whenever you go out | automate | pushcut, twilio | 🟢 Low | [92_Send_an_SMS_to_a_number_whenever_you_go_out.json](workflows/92_Send_an_SMS_to_a_number_whenever_you_go_out.json) |
| Send an SMS using MSG91 | automate | manual, msg91 | 🟢 Low | [511_Send_an_SMS_using_MSG91.json](workflows/511_Send_an_SMS_using_MSG91.json) |
| Send an SMS using the Mocean node | automate | mocean, manual | 🟢 Low | [59_Send_an_SMS_using_the_Mocean_node.json](workflows/59_Send_an_SMS_using_the_Mocean_node.json) |
| Smart Factory Use Case | automate | pagerduty, amqp, cratedb | 🟡 Medium | [168_Smart_Factory_Use_Case.json](workflows/168_Smart_Factory_Use_Case.json) |
| Snowflake CSV | automate | spreadsheetfile, httprequest, snowflake | 🟢 Low | [19_Snowflake_CSV.json](workflows/19_Snowflake_CSV.json) |
| Standup Bot - Initialize | automate | writebinaryfile, movebinarydata, manual | 🟢 Low | [111_Standup_Bot_-_Initialize.json](workflows/111_Standup_Bot_-_Initialize.json) |
| Standup Bot - Override Config | automate | writebinaryfile, movebinarydata, manual | 🟢 Low | [113_Standup_Bot_-_Override_Config.json](workflows/113_Standup_Bot_-_Override_Config.json) |
| TEMPLATES | automate | httprequest, manual, mondaycom | 🔴 High | [MmfWpcIegNgBjBpL_TEMPLATES.json](workflows/MmfWpcIegNgBjBpL_TEMPLATES.json) |
| TOTP VALIDATION (WITHOUT CREATING CREDENTIAL) | automate | manual | 🟢 Low | [2379_TOTP_VALIDATION_(WITHOUT_CREATING_CREDENTIAL).json](workflows/2379_TOTP_VALIDATION_(WITHOUT_CREATING_CREDENTIAL).json) |
| The Easiest Way to Send SMS Worldwide | automate | httprequest, manual | 🟢 Low | [Qpxx8UnnACBONNJu_The_Easiest_Way_to_Send_SMS_Worldwide.json](workflows/Qpxx8UnnACBONNJu_The_Easiest_Way_to_Send_SMS_Worldwide.json) |
| TheHive | automate | webhook, manual, signl4 | 🟡 Medium | [3_TheHive.json](workflows/3_TheHive.json) |
| Tiktok Downloader | automate | httprequest, manual, googledrive | 🟡 Medium | [aVienX696oMCH1DR_Tiktok_Downloader.json](workflows/aVienX696oMCH1DR_Tiktok_Downloader.json) |
| Todoist Weekly Review Template | automate | emailsend, httprequest, schedule | 🟡 Medium | [VLRbAr4OrtnHUU2l_Todoist_Weekly_Review_Template.json](workflows/VLRbAr4OrtnHUU2l_Todoist_Weekly_Review_Template.json) |
| Translate | automate | form, extractfromfile, converttofile | 🔴 High | [vssVsRO0FW6InbaY_Translate.json](workflows/vssVsRO0FW6InbaY_Translate.json) |
| Translate text from English to German | automate | manual, googletranslate | 🟢 Low | [92_Translate_text_from_English_to_German.json](workflows/92_Translate_text_from_English_to_German.json) |
| Turn on a light and set its brightness | automate | manual, philipshue | 🟢 Low | [58_Turn_on_a_light_and_set_its_brightness.json](workflows/58_Turn_on_a_light_and_set_its_brightness.json) |
| URL Pinger | automate | schedule, httprequest | 🟢 Low | [F2AEknC2Kc3ujuX4_URL_Pinger.json](workflows/F2AEknC2Kc3ujuX4_URL_Pinger.json) |
| User Request Management | automate | typeform, clickup | 🟡 Medium | [16_User_Request_Management.json](workflows/16_User_Request_Management.json) |
| Very quick quickstart | automate | manual, n8ntrainingcustomerdatastore | 🟢 Low | [1700_Very_quick_quickstart.json](workflows/1700_Very_quick_quickstart.json) |
| What To Eat | automate | emailsend, httprequest, cron | 🟡 Medium | [11_What_To_Eat.json](workflows/11_What_To_Eat.json) |
| Wordpress Form to Mautic | automate | mautic, webhook | 🟡 Medium | [jOI7FRhG1FkeqBLG_Wordpress_Form_to_Mautic.json](workflows/jOI7FRhG1FkeqBLG_Wordpress_Form_to_Mautic.json) |
| Workflow stats | automate | movebinarydata, sort, webhook | 🔴 High | [D0I76cew5KOnlem0_Workflow_stats.json](workflows/D0I76cew5KOnlem0_Workflow_stats.json) |
| Write a file to the host machine | automate | writebinaryfile, httprequest, manual | 🟢 Low | [160_Write_a_file_to_the_host_machine.json](workflows/160_Write_a_file_to_the_host_machine.json) |
| Zammad Open Tickets | automate | zulip, manual, cron | 🟢 Low | [4_Zammad_Open_Tickets.json](workflows/4_Zammad_Open_Tickets.json) |
| Zip multiple files | automate | compression, executeworkflow | 🟢 Low | [r3qHlCVCczqTw3pP_Zip_multiple_files.json](workflows/r3qHlCVCczqTw3pP_Zip_multiple_files.json) |
| [n8n] YouTube Channel Advanced RSS Feeds Generator | automate | httprequest, form, respondtowebhook | 🔴 High | [2221_[n8n]_YouTube_Channel_Advanced_RSS_Feeds_Generator.json](workflows/2221_[n8n]_YouTube_Channel_Advanced_RSS_Feeds_Generator.json) |
| comentarios automaticos | automate | httprequest, webhook, n8n-nodes-langchain.lmchatopenrouter | 🔴 High | [4rXRDurF4mQKrHyB_comentarios_automaticos.json](workflows/4rXRDurF4mQKrHyB_comentarios_automaticos.json) |
| dub.co URL Shortener | automate | httprequest, manual | 🟡 Medium | [ReXF4z8ZKcEd6Kea_dub.co_URL_Shortener.json](workflows/ReXF4z8ZKcEd6Kea_dub.co_URL_Shortener.json) |
| itemMatching() example | automate | n8ntrainingcustomerdatastore, manual | 🟡 Medium | [gkOayLvJnwcTiHbk_itemMatching()_example.json](workflows/gkOayLvJnwcTiHbk_itemMatching()_example.json) |
| location_by_ip | automate | awsses, uproc, functionitem | 🟡 Medium | [104_location_by_ip.json](workflows/104_location_by_ip.json) |
| n8n Subworkflow Dependency Graph & Auto-Tagging | automate | splitinbatches, respondtowebhook, quickchart | 🔴 High | [P9Jr9s9yfcDXTe9R_n8n_Subworkflow_Dependency_Graph_&_Auto-Tagging.json](workflows/P9Jr9s9yfcDXTe9R_n8n_Subworkflow_Dependency_Graph_&_Auto-Tagging.json) |
| pdf to text | automate | manual | 🟢 Low | [MIA4ozGH71fC3KCe_pdf_to_text.json](workflows/MIA4ozGH71fC3KCe_pdf_to_text.json) |
| ppsHlJlSpHPQJp4Q_workflow_ppsHlJlSpHPQJp4Q | automate | schedule, httprequest, twilio | 🟢 Low | [ppsHlJlSpHPQJp4Q_workflow_ppsHlJlSpHPQJp4Q.json](workflows/ppsHlJlSpHPQJp4Q_workflow_ppsHlJlSpHPQJp4Q.json) |
| screenshot | automate | awsses, uproc, httprequest | 🟡 Medium | [105_screenshot.json](workflows/105_screenshot.json) |
| v1 helper - Find params with affected expressions | automate | n8n, manual | 🟢 Low | [zlHbtHIcCZ9enKwg_v1_helper_-_Find_params_with_affected_expressions.json](workflows/zlHbtHIcCZ9enKwg_v1_helper_-_Find_params_with_affected_expressions.json) |
| x2VUvhqV1YTJCIN0_workflow_x2VUvhqV1YTJCIN0 | automate | httprequest, graphql, webhook | 🟡 Medium | [x2VUvhqV1YTJCIN0_workflow_x2VUvhqV1YTJCIN0.json](workflows/x2VUvhqV1YTJCIN0_workflow_x2VUvhqV1YTJCIN0.json) |
| 💻 Schedule workflow activity time | automate | schedule, n8n | 🟡 Medium | [cGqPi5Uy2u1ShmoO_💻_Schedule_workflow_activity_time.json](workflows/cGqPi5Uy2u1ShmoO_💻_Schedule_workflow_activity_time.json) |
| 🦙👁️👁️ Find the Best Local Ollama Vision Models by Comparison | automate | splitinbatches, googledocs, httprequest | 🔴 High | [keFEBUqHOrsib60G_🦙👁️👁️_Find_the_Best_Local_Ollama_Vision_Models_by_Comparison.json](workflows/keFEBUqHOrsib60G_🦙👁️👁️_Find_the_Best_Local_Ollama_Vision_Models_by_Comparison.json) |
| Backup n8n Workflows to Bitbucket | backup | splitinbatches, httprequest, schedule | 🟡 Medium | [23GPrqZjHnIVvTEa_Backup_n8n_Workflows_to_Bitbucket.json](workflows/23GPrqZjHnIVvTEa_Backup_n8n_Workflows_to_Bitbucket.json) |
| Backup workflows to git repository on Gitea | backup | splitinbatches, httprequest, schedule | 🔴 High | [Ef2uEM6H19K2DGUO_Backup_workflows_to_git_repository_on_Gitea.json](workflows/Ef2uEM6H19K2DGUO_Backup_workflows_to_git_repository_on_Gitea.json) |
| Example - Backup n8n to Nextcloud | backup | movebinarydata, httprequest, functionitem | 🟡 Medium | [5dcd71e5db772d996680f0be_Example_-_Backup_n8n_to_Nextcloud.json](workflows/5dcd71e5db772d996680f0be_Example_-_Backup_n8n_to_Nextcloud.json) |
| Tools / Backup Gitlab | backup | cron, manual, executecommand | 🟢 Low | [15_Tools___Backup_Gitlab.json](workflows/15_Tools___Backup_Gitlab.json) |
| Add a event to Calender | create | googlecalendar, manual | 🟢 Low | [1_Add_a_event_to_Calender.json](workflows/1_Add_a_event_to_Calender.json) |
| Add text to an image downloaded from the internet | create | httprequest, editimage, manual | 🟢 Low | [1_Add_text_to_an_image_downloaded_from_the_internet.json](workflows/1_Add_text_to_an_image_downloaded_from_the_internet.json) |
| Create Google Creds | create | manual, n8n | 🟡 Medium | [fEJliGTxbsE0G8z2_Create_Google_Creds.json](workflows/fEJliGTxbsE0G8z2_Create_Google_Creds.json) |
| Create Threads on Bluesky | create | splitinbatches, httprequest, schedule | 🔴 High | [7ZIG5xxEACMBgj4Z_Create_Threads_on_Bluesky.json](workflows/7ZIG5xxEACMBgj4Z_Create_Threads_on_Bluesky.json) |
| Create a client in Harvest | create | manual, harvest | 🟢 Low | [120_Create_a_client_in_Harvest.json](workflows/120_Create_a_client_in_Harvest.json) |
| Create a coupon on Paddle | create | paddle, manual | 🟢 Low | [54_Create_a_coupon_on_Paddle.json](workflows/54_Create_a_coupon_on_Paddle.json) |
| Create a new card in Trello | create | trello, manual | 🟢 Low | [89_Create_a_new_card_in_Trello.json](workflows/89_Create_a_new_card_in_Trello.json) |
| Create a project, tag, and time entry, and update the time entry in Clockify | create | manual, clockify | 🟢 Low | [76_Create_a_project,_tag,_and_time_entry,_and_update_the_time_entry_in_Clockify.json](workflows/76_Create_a_project,_tag,_and_time_entry,_and_update_the_time_entry_in_Clockify.json) |
| Create a release and get all releases | create | manual, sentryio | 🟢 Low | [27_Create_a_release_and_get_all_releases.json](workflows/27_Create_a_release_and_get_all_releases.json) |
| Create a short URL and get the statistics of the URL | create | manual, yourls | 🟢 Low | [167_Create_a_short_URL_and_get_the_statistics_of_the_URL.json](workflows/167_Create_a_short_URL_and_get_the_statistics_of_the_URL.json) |
| Create an organization in Affinity | create | affinity, manual | 🟢 Low | [95_Create_an_organization_in_Affinity.json](workflows/95_Create_an_organization_in_Affinity.json) |
| Create dynamic Twitter profile banner | create | editimage, itemlists, httprequest | 🟡 Medium | [Create dynamic Twitter profile banner.json](workflows/Create dynamic Twitter profile banner.json) |
| Create, update and get a case in TheHive | create | manual, thehive | 🟢 Low | [159_Create,_update_and_get_a_case_in_TheHive.json](workflows/159_Create,_update_and_get_a_case_in_TheHive.json) |
| Create, update and get records in Quick Base | create | quickbase, manual | 🟢 Low | [156_Create,_update_and_get_records_in_Quick_Base.json](workflows/156_Create,_update_and_get_records_in_Quick_Base.json) |
| Create, update, and get a subscriber using the e-goi node | create | manual, egoi | 🟢 Low | [189_Create,_update,_and_get_a_subscriber_using_the_e-goi_node.json](workflows/189_Create,_update,_and_get_a_subscriber_using_the_e-goi_node.json) |
| Create, update, and get activity in Strava | create | strava, manual | 🟢 Low | [93_Create,_update,_and_get_activity_in_Strava.json](workflows/93_Create,_update,_and_get_activity_in_Strava.json) |
| Create, update, and get an incident on PagerDuty | create | pagerduty, manual | 🟢 Low | [158_Create,_update,_and_get_an_incident_on_PagerDuty.json](workflows/158_Create,_update,_and_get_an_incident_on_PagerDuty.json) |
| Get a volume and add it to your bookshelf | create | manual, googlebooks | 🟢 Low | [107_Get_a_volume_and_add_it_to_your_bookshelf.json](workflows/107_Get_a_volume_and_add_it_to_your_bookshelf.json) |
| Receive updates when a new list is created in Affinity | create | affinity | 🟢 Low | [63_Receive_updates_when_a_new_list_is_created_in_Affinity.json](workflows/63_Receive_updates_when_a_new_list_is_created_in_Affinity.json) |
| address validation | create | httprequest, webhook | 🔴 High | [VaU41OXvni95OlAL_address_validation.json](workflows/VaU41OXvni95OlAL_address_validation.json) |
| Create a contact in Drift | create_contact | drift, manual | 🟢 Low | [125_Create_a_contact_in_Drift.json](workflows/125_Create_a_contact_in_Drift.json) |
| Create a new list, add a new contact to the list, update the contact, and get all contacts in the list | create_contact | manual, automizy | 🟢 Low | [82_Create_a_new_list,_add_a_new_contact_to_the_list,_update_the_contact,_and_get_all_contacts_in_the_list.json](workflows/82_Create_a_new_list,_add_a_new_contact_to_the_list,_update_the_contact,_and_get_all_contacts_in_the_list.json) |
| Create a new user in Intercom | create_contact | manual, intercom | 🟢 Low | [91_Create_a_new_user_in_Intercom.json](workflows/91_Create_a_new_user_in_Intercom.json) |
| Create a user profile in Vero | create_contact | vero, manual | 🟢 Low | [127_Create_a_user_profile_in_Vero.json](workflows/127_Create_a_user_profile_in_Vero.json) |
| Create, update and get a contact in Google Contacts | create_contact | googlecontacts, manual | 🟢 Low | [20_Create,_update_and_get_a_contact_in_Google_Contacts.json](workflows/20_Create,_update_and_get_a_contact_in_Google_Contacts.json) |
| Create, update and get a user from Iterable | create_contact | manual, iterable | 🟢 Low | [165_Create,_update_and_get_a_user_from_Iterable.json](workflows/165_Create,_update_and_get_a_user_from_Iterable.json) |
| Create, update, and get a user using the G Suite Admin node | create_contact | gsuiteadmin, manual | 🟢 Low | [215_Create,_update,_and_get_a_user_using_the_G_Suite_Admin_node.json](workflows/215_Create,_update,_and_get_a_user_using_the_G_Suite_Admin_node.json) |
| Add task to tasklist | create_task | googletasks, manual | 🟢 Low | [2_Add_task_to_tasklist.json](workflows/2_Add_task_to_tasklist.json) |
| Create a new issue in Jira | create_task | jira, manual | 🟢 Low | [87_Create_a_new_issue_in_Jira.json](workflows/87_Create_a_new_issue_in_Jira.json) |
| Create a new task in Asana | create_task | manual, asana | 🟢 Low | [98_Create_a_new_task_in_Asana.json](workflows/98_Create_a_new_task_in_Asana.json) |
| Create a new task in Todoist | create_task | todoist, manual | 🟢 Low | [100_Create_a_new_task_in_Todoist.json](workflows/100_Create_a_new_task_in_Todoist.json) |
| Create a task in ClickUp | create_task | clickup, manual | 🟢 Low | [105_Create_a_task_in_ClickUp.json](workflows/105_Create_a_task_in_ClickUp.json) |
| Create a ticket in Zendesk | create_task | manual, zendesk | 🟢 Low | [123_Create_a_ticket_in_Zendesk.json](workflows/123_Create_a_ticket_in_Zendesk.json) |
| Create an Onfleet task when a file in Google Drive is updated | create_task | onfleet, googledrive | 🟢 Low | [1547_Create_an_Onfleet_task_when_a_file_in_Google_Drive_is_updated.json](workflows/1547_Create_an_Onfleet_task_when_a_file_in_Google_Drive_is_updated.json) |
| Remove Advanced Background from Google Drive Images | delete | splitinbatches, httprequest, googledrive | 🔴 High | [oNJCLq4egGByMeSl_Remove_Advanced_Background_from_Google_Drive_Images.json](workflows/oNJCLq4egGByMeSl_Remove_Advanced_Background_from_Google_Drive_Images.json) |
| Remove Advanced Background from Google Drive Images | delete | splitinbatches, httprequest, googledrive | 🔴 High | [Automatic Background Removal for Images in Google Drive.json](workflows/Automatic Background Removal for Images in Google Drive.json) |
| Extract And Decode Google News RSS URLs to Clean Article Links | extract | httprequest, rssfeedread, manual | 🔴 High | [3JsfhcDcjqxx0hr3_Extract_And_Decode_Google_News_RSS_URLs_to_Clean_Article_Links.json](workflows/3JsfhcDcjqxx0hr3_Extract_And_Decode_Google_News_RSS_URLs_to_Clean_Article_Links.json) |
| Extract information from an image of a receipt | extract | mindee, httprequest, manual | 🟢 Low | [77_Extract_information_from_an_image_of_a_receipt.json](workflows/77_Extract_information_from_an_image_of_a_receipt.json) |
| Google Page Entity Extraction Template | extract | httprequest, webhook, respondtowebhook | 🟡 Medium | [4wPgPbxtojrUO7Dx_Google_Page_Entity_Extraction_Template.json](workflows/4wPgPbxtojrUO7Dx_Google_Page_Entity_Extraction_Template.json) |
| Scrape Latest 20 TechCrunch Articles | extract | httprequest, manual, html | 🟡 Medium | [MKGrRFnUuMZMAxNf_Scrape_Latest_20_TechCrunch_Articles.json](workflows/MKGrRFnUuMZMAxNf_Scrape_Latest_20_TechCrunch_Articles.json) |
| Scrape Today's Github Trend 13 Top Repositories | extract | httprequest, manual, html | 🟡 Medium | [BXfxO6faULfsy2JN_Scrape_Today's_Github_Trend_13_Top_Repositories.json](workflows/BXfxO6faULfsy2JN_Scrape_Today's_Github_Trend_13_Top_Repositories.json) |
| Generate Image Workflow | generate | httprequest, manual | 🟢 Low | [2990_Generate_Image_Workflow.json](workflows/2990_Generate_Image_Workflow.json) |
| Generate Text-to-Speech Using Elevenlabs via API | generate | httprequest, webhook, respondtowebhook | 🟡 Medium | [Generate Text-to-Speech Using Elevenlabs via API.json](workflows/Generate Text-to-Speech Using Elevenlabs via API.json) |
| Motion-illustration Workflow Generated with Midjourney and Kling API | generate | httprequest, manual | 🟡 Medium | [HBUhVkSsjslXAojw_Motion-illustration_Workflow_Generated_with_Midjourney_and_Kling_API.json](workflows/HBUhVkSsjslXAojw_Motion-illustration_Workflow_Generated_with_Midjourney_and_Kling_API.json) |
| Bitrix24 Task Form Widget Application Workflow example with Webhook Integration | read | httprequest, readwritefile, webhook | 🔴 High | [ZDL9028SnyCxS5tf_Bitrix24_Task_Form_Widget_Application_Workflow_example_with_Webhook_Integration.json](workflows/ZDL9028SnyCxS5tf_Bitrix24_Task_Form_Widget_Application_Workflow_example_with_Webhook_Integration.json) |
| Convert Parquet, Avro, ORC & Feather via ParquetReader to JSON | read | webhook, httprequest | 🟢 Low | [VU0kmvnWzctSFm2M_Convert_Parquet,_Avro,_ORC_&_Feather_via_ParquetReader_to_JSON.json](workflows/VU0kmvnWzctSFm2M_Convert_Parquet,_Avro,_ORC_&_Feather_via_ParquetReader_to_JSON.json) |
| Get Company by Name | read | functionitem, uproc, manual | 🟢 Low | [112_Get_Company_by_Name.json](workflows/112_Get_Company_by_Name.json) |
| Get DNS entries | read | functionitem, uproc, manual | 🟢 Low | [113_Get_DNS_entries.json](workflows/113_Get_DNS_entries.json) |
| Get Long Lived Facebook User or Page Access Token | read | httprequest, manual | 🟢 Low | [iA0rm7IWi7xmY5sQ_Get_Long_Lived_Facebook_User_or_Page_Access_Token.json](workflows/iA0rm7IWi7xmY5sQ_Get_Long_Lived_Facebook_User_or_Page_Access_Token.json) |
| Get a pipeline in CircleCI | read | circleci, manual | 🟢 Low | [84_Get_a_pipeline_in_CircleCI.json](workflows/84_Get_a_pipeline_in_CircleCI.json) |
| Get all scaleway server info copy | read | splitinbatches, httprequest, webhook | 🔴 High | [olDVR3wuxbUsTvuW_Get_all_scaleway_server_info_copy.json](workflows/olDVR3wuxbUsTvuW_Get_all_scaleway_server_info_copy.json) |
| Get all the stories starting with `release` and publish them | read | storyblok, manual | 🟢 Low | [110_Get_all_the_stories_starting_with_`release`_and_publish_them.json](workflows/110_Get_all_the_stories_starting_with_`release`_and_publish_them.json) |
| Get all the tasks in Flow | read | flow, manual | 🟢 Low | [130_Get_all_the_tasks_in_Flow.json](workflows/130_Get_all_the_tasks_in_Flow.json) |
| Get new time entries from Toggl | read | toggl | 🟢 Low | [138_Get_new_time_entries_from_Toggl.json](workflows/138_Get_new_time_entries_from_Toggl.json) |
| Get only new RSS with Photo | read | htmlextract, rssfeedread, cron | 🟢 Low | [8_Get_only_new_RSS_with_Photo.json](workflows/8_Get_only_new_RSS_with_Photo.json) |
| Get synonyms of a German word | read | manual, openthesaurus | 🟢 Low | [157_Get_synonyms_of_a_German_word.json](workflows/157_Get_synonyms_of_a_German_word.json) |
| Get the price of BTC in EUR and send an SMS when the price is larger than EUR 9000 | read | coingecko, cron, twilio | 🟢 Low | [79_Get_the_price_of_BTC_in_EUR_and_send_an_SMS_when_the_price_is_larger_than_EUR_9000.json](workflows/79_Get_the_price_of_BTC_in_EUR_and_send_an_SMS_when_the_price_is_larger_than_EUR_9000.json) |
| Get today's date and day using the Function node | read | manual | 🟢 Low | [140_Get_today's_date_and_day_using_the_Function_node.json](workflows/140_Get_today's_date_and_day_using_the_Function_node.json) |
| MONDAY GET FULL ITEM | read | mondaycom, executeworkflow, executeworkflow | 🔴 High | [ZdGZh4qmOqTQe1oq_MONDAY_GET_FULL_ITEM.json](workflows/ZdGZh4qmOqTQe1oq_MONDAY_GET_FULL_ITEM.json) |
| Read RSS feed from two different sources | read | splitinbatches, manual, rssfeedread | 🟢 Low | [7604ck94MeYXMHpN_Read_RSS_feed_from_two_different_sources.json](workflows/7604ck94MeYXMHpN_Read_RSS_feed_from_two_different_sources.json) |
| Read sitemap and filter URLs | read | httprequest, xml, manual | 🟡 Medium | [7fdJOvYNILCr24fH_Read_sitemap_and_filter_URLs.json](workflows/7fdJOvYNILCr24fH_Read_sitemap_and_filter_URLs.json) |
| Standup Bot - Read Config | read | movebinarydata, manual, readbinaryfile | 🟢 Low | [112_Standup_Bot_-_Read_Config.json](workflows/112_Standup_Bot_-_Read_Config.json) |
| Telegram channel to Readeck & Hoarder | read | httprequest, schedule | 🔴 High | [Gd4MsAZGnSGfBwaw_Telegram_channel_to_Readeck_&_Hoarder.json](workflows/Gd4MsAZGnSGfBwaw_Telegram_channel_to_Readeck_&_Hoarder.json) |
| Upload a file and get a list of all the files in a bucket | read | httprequest, manual | 🟢 Low | [64_Upload_a_file_and_get_a_list_of_all_the_files_in_a_bucket.json](workflows/64_Upload_a_file_and_get_a_list_of_all_the_files_in_a_bucket.json) |
| getBible Query v1.0 | read | httprequest, executeworkflow | 🟢 Low | [gqwYlZvL1dwy9W3T_getBible_Query_v1.0.json](workflows/gqwYlZvL1dwy9W3T_getBible_Query_v1.0.json) |
| get_a_web_page | read | httprequest, executeworkflow | 🟢 Low | [Using External Workflows as Tools in n8n.json](workflows/Using External Workflows as Tools in n8n.json) |
| get_a_web_page | read | httprequest, executeworkflow | 🟢 Low | [7DPLpEkww5Uctcml_get_a_web_page.json](workflows/7DPLpEkww5Uctcml_get_a_web_page.json) |
| Credentials Transfer | transfer | httprequest, executecommand, form | 🔴 High | [tlnJNm9t5H3VLU5K_Credentials_Transfer.json](workflows/tlnJNm9t5H3VLU5K_Credentials_Transfer.json) |
| Export Zammad Objects Users, Roles, Groups and Organizations to Excel | transfer | httprequest, manual, zammad | 🔴 High | [IXumIzS9WtPAhKFX_Export_Zammad_Objects_Users,_Roles,_Groups_and_Organizations_to_Excel.json](workflows/IXumIzS9WtPAhKFX_Export_Zammad_Objects_Users,_Roles,_Groups_and_Organizations_to_Excel.json) |
| Import CSV from URL to Excel | transfer | spreadsheetfile, httprequest, manual | 🟢 Low | [xcl8D1sukz9Rak69_Import_CSV_from_URL_to_Excel.json](workflows/xcl8D1sukz9Rak69_Import_CSV_from_URL_to_Excel.json) |
| Workflow Importer | transfer | httprequest, executecommand, readwritefile | 🔴 High | [87FUCRVFV07sNlbM_Workflow_Importer.json](workflows/87FUCRVFV07sNlbM_Workflow_Importer.json) |
| Automate Figma Versioning and Jira Updates with n8n Webhook Integration | update | jira, figma | 🟢 Low | [5kYHogzDGeo21MxE_Automate_Figma_Versioning_and_Jira_Updates_with_n8n_Webhook_Integration.json](workflows/5kYHogzDGeo21MxE_Automate_Figma_Versioning_and_Jira_Updates_with_n8n_Webhook_Integration.json) |
| Get all the contacts from GetResponse and update them | update | getresponse, manual | 🟢 Low | [116_Get_all_the_contacts_from_GetResponse_and_update_them.json](workflows/116_Get_all_the_contacts_from_GetResponse_and_update_them.json) |
| Receive updates for changes in the specified list in Trello | update | trello | 🟢 Low | [117_Receive_updates_for_changes_in_the_specified_list_in_Trello.json](workflows/117_Receive_updates_for_changes_in_the_specified_list_in_Trello.json) |
| Receive updates for events in ClickUp | update | clickup | 🟢 Low | [110_Receive_updates_for_events_in_ClickUp.json](workflows/110_Receive_updates_for_events_in_ClickUp.json) |
| Receive updates for specified tasks in Flow | update | flow | 🟢 Low | [133_Receive_updates_for_specified_tasks_in_Flow.json](workflows/133_Receive_updates_for_specified_tasks_in_Flow.json) |
| Receive updates for support in Zendesk | update | zendesk | 🟢 Low | [33_Receive_updates_for_support_in_Zendesk.json](workflows/33_Receive_updates_for_support_in_Zendesk.json) |
| Receive updates when a form is submitted in Mautic, and send a confirmation SMS | update | mautic, twilio | 🟢 Low | [13_Receive_updates_when_a_form_is_submitted_in_Mautic,_and_send_a_confirmation_SMS.json](workflows/13_Receive_updates_when_a_form_is_submitted_in_Mautic,_and_send_a_confirmation_SMS.json) |
| Receive updates when a form is submitted in Wufoo | update | wufoo | 🟢 Low | [78_Receive_updates_when_a_form_is_submitted_in_Wufoo.json](workflows/78_Receive_updates_when_a_form_is_submitted_in_Wufoo.json) |
| Receive updates when a form submission occurs in your Webflow website | update | webflow | 🟢 Low | [42_Receive_updates_when_a_form_submission_occurs_in_your_Webflow_website.json](workflows/42_Receive_updates_when_a_form_submission_occurs_in_your_Webflow_website.json) |
| Receive updates when a sale is made in Gumroad | update | gumroad | 🟢 Low | [34_Receive_updates_when_a_sale_is_made_in_Gumroad.json](workflows/34_Receive_updates_when_a_sale_is_made_in_Gumroad.json) |
| Receive updates when an event occurs in Asana | update | asana | 🟢 Low | [47_Receive_updates_when_an_event_occurs_in_Asana.json](workflows/47_Receive_updates_when_an_event_occurs_in_Asana.json) |
| Receive updates when an event occurs in TheHive | update | thehive | 🟢 Low | [161_Receive_updates_when_an_event_occurs_in_TheHive.json](workflows/161_Receive_updates_when_an_event_occurs_in_TheHive.json) |
| Send updates about the position of the ISS every minute to a topic in ActiveMQ | update | amqp, httprequest, cron | 🟢 Low | [102_Send_updates_about_the_position_of_the_ISS_every_minute_to_a_topic_in_ActiveMQ.json](workflows/102_Send_updates_about_the_position_of_the_ISS_every_minute_to_a_topic_in_ActiveMQ.json) |
| Send updates about the position of the ISS every minute to a topic in Kafka | update | httprequest, kafka, cron | 🟢 Low | [98_Send_updates_about_the_position_of_the_ISS_every_minute_to_a_topic_in_Kafka.json](workflows/98_Send_updates_about_the_position_of_the_ISS_every_minute_to_a_topic_in_Kafka.json) |
| Send updates about the position of the ISS every minute to a topic in RabbitMQ | update | rabbitmq, httprequest, cron | 🟢 Low | [184_Send_updates_about_the_position_of_the_ISS_every_minute_to_a_topic_in_RabbitMQ.json](workflows/184_Send_updates_about_the_position_of_the_ISS_every_minute_to_a_topic_in_RabbitMQ.json) |
| Update Roles by Excel | update | httprequest, manual, extractfromfile | 🟡 Medium | [xzKlhjcc6QEzA98Z_Update_Roles_by_Excel.json](workflows/xzKlhjcc6QEzA98Z_Update_Roles_by_Excel.json) |
| Update Twitter banner using HTTP request | update | start, httprequest, manual | 🟢 Low | [Update Twitter banner using HTTP request.json](workflows/Update Twitter banner using HTTP request.json) |
| Update all Zammad Roles to default values | update | httprequest, manual, zammad | 🟡 Medium | [cDmsWx8ASzIxE3zw_Update_all_Zammad_Roles_to_default_values.json](workflows/cDmsWx8ASzIxE3zw_Update_all_Zammad_Roles_to_default_values.json) |
| Slack Webhook - Verify Signature | validate | crypto, stopanderror, executeworkflow | 🟡 Medium | [84dT8cFL0FV8ZGPx_Slack_Webhook_-_Verify_Signature.json](workflows/84dT8cFL0FV8ZGPx_Slack_Webhook_-_Verify_Signature.json) |
| Verify phone numbers | validate | functionitem, uproc, manual | 🟢 Low | [114_Verify_phone_numbers.json](workflows/114_Verify_phone_numbers.json) |

## COMM

*281 workflows in this category*

| Workflow Name | Business Function | Key Integrations | Complexity | File |
|---------------|-------------------|------------------|------------|------|
| Analyze feedback using AWS Comprehend and send it to a Mattermost channel | analyze | awscomprehend, mattermost, typeform | 🟢 Low | [Analyze feedback using AWS Comprehend and send it to a Mattermost channel.json](workflows/Analyze feedback using AWS Comprehend and send it to a Mattermost channel.json) |
| Analyze the sentiment of feedback and send a message on Mattermost | analyze | googlecloudnaturallanguage, mattermost, typeform | 🟢 Low | [133_Analyze_the_sentiment_of_feedback_and_send_a_message_on_Mattermost.json](workflows/133_Analyze_the_sentiment_of_feedback_and_send_a_message_on_Mattermost.json) |
| Analyze the sentiment of feedback and send a message on Mattermost | analyze | googlecloudnaturallanguage, mattermost, typeform | 🟢 Low | [Analyze feedback and send a message on Mattermost.json](workflows/Analyze feedback and send a message on Mattermost.json) |
| Analyze_Crowdstrike_Detections__search_for_IOCs_in_VirusTotal__create_a_ticket_in_Jira_and_post_a_message_in_Slack | analyze | splitinbatches, itemlists, slack | 🔴 High | [IMVycpyABaGuD1hq_Analyze_Crowdstrike_Detections__search_for_IOCs_in_VirusTotal__create_a_ticket_in_Jira_and_post_a_message_in_Slack.json](workflows/IMVycpyABaGuD1hq_Analyze_Crowdstrike_Detections__search_for_IOCs_in_VirusTotal__create_a_ticket_in_Jira_and_post_a_message_in_Slack.json) |
| 1039_workflow_1039 | automate | emelia, mattermost | 🟢 Low | [1039_workflow_1039.json](workflows/1039_workflow_1039.json) |
| 1041_workflow_1041 | automate | emelia, mattermost | 🟢 Low | [1041_workflow_1041.json](workflows/1041_workflow_1041.json) |
| 1058_workflow_1058 | automate | n8n, mattermost | 🟢 Low | [1058_workflow_1058.json](workflows/1058_workflow_1058.json) |
| 1059_workflow_1059 | automate | webhook, workflow, mattermost | 🟢 Low | [1059_workflow_1059.json](workflows/1059_workflow_1059.json) |
| 1078_workflow_1078 | automate | gmail, googledrive | 🟢 Low | [1078_workflow_1078.json](workflows/1078_workflow_1078.json) |
| 1089_workflow_1089 | automate | notion, mattermost | 🟢 Low | [1089_workflow_1089.json](workflows/1089_workflow_1089.json) |
| 1109_workflow_1109 | automate | slack, googlecloudnaturallanguage, trello | 🟡 Medium | [1109_workflow_1109.json](workflows/1109_workflow_1109.json) |
| 1134_workflow_1134 | automate | telegram, github | 🟢 Low | [1134_workflow_1134.json](workflows/1134_workflow_1134.json) |
| 1153_workflow_1153 | automate | splitinbatches, gmail, manual | 🟢 Low | [1153_workflow_1153.json](workflows/1153_workflow_1153.json) |
| 1205_workflow_1205 | automate | shopify, telegram, twitter | 🟢 Low | [1205_workflow_1205.json](workflows/1205_workflow_1205.json) |
| 1206_workflow_1206 | automate | zohocrm, trello, gmail | 🟡 Medium | [1206_workflow_1206.json](workflows/1206_workflow_1206.json) |
| 1207_workflow_1207 | automate | slack, shopify, datetime | 🟡 Medium | [1207_workflow_1207.json](workflows/1207_workflow_1207.json) |
| 1216_workflow_1216 | automate | googleperspective, telegram, telegram | 🟢 Low | [1216_workflow_1216.json](workflows/1216_workflow_1216.json) |
| 1221_workflow_1221 | automate | pipedrive, calendly, slack | 🟢 Low | [1221_workflow_1221.json](workflows/1221_workflow_1221.json) |
| 1223_workflow_1223 | automate | hubspot, gmail, typeform | 🟡 Medium | [1223_workflow_1223.json](workflows/1223_workflow_1223.json) |
| 1225_workflow_1225 | automate | hubspot, googleslides, slack | 🟡 Medium | [1225_workflow_1225.json](workflows/1225_workflow_1225.json) |
| 1255_workflow_1255 | automate | slack, netlify | 🟢 Low | [1255_workflow_1255.json](workflows/1255_workflow_1255.json) |
| 1277_workflow_1277 | automate | slack, datetime, googlecalendar | 🟡 Medium | [1277_workflow_1277.json](workflows/1277_workflow_1277.json) |
| 1298_workflow_1298 | automate | itemlists, graphql, cron | 🟢 Low | [1298_workflow_1298.json](workflows/1298_workflow_1298.json) |
| 1324_workflow_1324 | automate | slack, dropcontact, airtable | 🟡 Medium | [1324_workflow_1324.json](workflows/1324_workflow_1324.json) |
| 1326_workflow_1326 | automate | error, slack | 🟢 Low | [1326_workflow_1326.json](workflows/1326_workflow_1326.json) |
| 1364_workflow_1364 | automate | webhook, manual, telegram | 🟡 Medium | [1364_workflow_1364.json](workflows/1364_workflow_1364.json) |
| 1381_workflow_1381 | automate | httprequest, functionitem, webhook | 🟡 Medium | [1381_workflow_1381.json](workflows/1381_workflow_1381.json) |
| 1393_workflow_1393 | automate | awstextract, telegram, airtable | 🟢 Low | [1393_workflow_1393.json](workflows/1393_workflow_1393.json) |
| 1416_workflow_1416 | automate | httprequest, functionitem, manual | 🔴 High | [1416_workflow_1416.json](workflows/1416_workflow_1416.json) |
| 1425_workflow_1425 | automate | cron, httprequest, telegram | 🔴 High | [1425_workflow_1425.json](workflows/1425_workflow_1425.json) |
| 1463_workflow_1463 | automate | hubspot, slack, httprequest | 🟢 Low | [1463_workflow_1463.json](workflows/1463_workflow_1463.json) |
| 1471_workflow_1471 | automate | httprequest, telegram, cron | 🟡 Medium | [1471_workflow_1471.json](workflows/1471_workflow_1471.json) |
| 1534_workflow_1534 | automate | splitinbatches, slack, httprequest | 🔴 High | [1534_workflow_1534.json](workflows/1534_workflow_1534.json) |
| 1554_workflow_1554 | automate | splitinbatches, rssfeedread, telegram | 🟡 Medium | [1554_workflow_1554.json](workflows/1554_workflow_1554.json) |
| 1570_workflow_1570 | automate | slack, httprequest, manual | 🟢 Low | [1570_workflow_1570.json](workflows/1570_workflow_1570.json) |
| 1583_workflow_1583 | automate | nocodb, httprequest, telegram | 🔴 High | [1583_workflow_1583.json](workflows/1583_workflow_1583.json) |
| 1599_workflow_1599 | automate | interval, telegram, youtube | 🟢 Low | [1599_workflow_1599.json](workflows/1599_workflow_1599.json) |
| 1605_workflow_1605 | automate | spreadsheetfile, httprequest, executecommand | 🔴 High | [1605_workflow_1605.json](workflows/1605_workflow_1605.json) |
| 1734_workflow_1734 | automate | spreadsheetfile, gmail, movebinarydata | 🟢 Low | [1734_workflow_1734.json](workflows/1734_workflow_1734.json) |
| 1739_workflow_1739 | automate | spreadsheetfile, gmail, writebinaryfile | 🔴 High | [1739_workflow_1739.json](workflows/1739_workflow_1739.json) |
| 1770_workflow_1770 | automate | hubspot, mailchimp, cron | 🟢 Low | [1770_workflow_1770.json](workflows/1770_workflow_1770.json) |
| 1771_workflow_1771 | automate | functionitem, hubspot, mailchimp | 🟢 Low | [1771_workflow_1771.json](workflows/1771_workflow_1771.json) |
| 1785_workflow_1785 | automate | htmlextract, sendgrid, httprequest | 🟡 Medium | [1785_workflow_1785.json](workflows/1785_workflow_1785.json) |
| 1820_workflow_1820 | automate | slack, webhook, zendesk | 🟡 Medium | [1820_workflow_1820.json](workflows/1820_workflow_1820.json) |
| 1891_workflow_1891 | automate | hubspot, slack, lemlist | 🔴 High | [1891_workflow_1891.json](workflows/1891_workflow_1891.json) |
| 1931_workflow_1931 | automate | slack, itemlists, notion | 🟡 Medium | [1931_workflow_1931.json](workflows/1931_workflow_1931.json) |
| 1932_workflow_1932 | automate | linear, slack, manual | 🟡 Medium | [1932_workflow_1932.json](workflows/1932_workflow_1932.json) |
| 1939_workflow_1939 | automate | datetime, gmail, httprequest | 🔴 High | [1939_workflow_1939.json](workflows/1939_workflow_1939.json) |
| 1941_workflow_1941 | automate | discord, googlesheets | 🟢 Low | [1941_workflow_1941.json](workflows/1941_workflow_1941.json) |
| 1971_workflow_1971 | automate | itemlists, slack, gmail | 🔴 High | [1971_workflow_1971.json](workflows/1971_workflow_1971.json) |
| 1999_workflow_1999 | automate | telegram, n8n | 🟡 Medium | [1999_workflow_1999.json](workflows/1999_workflow_1999.json) |
| 2023_workflow_2023 | automate | itemlists, slack, httprequest | 🔴 High | [2023_workflow_2023.json](workflows/2023_workflow_2023.json) |
| 2043_workflow_2043 | automate | httprequest, schedule, telegram | 🟡 Medium | [2043_workflow_2043.json](workflows/2043_workflow_2043.json) |
| 2045_workflow_2045 | automate | splitinbatches, httprequest, telegram | 🔴 High | [2045_workflow_2045.json](workflows/2045_workflow_2045.json) |
| 2050_workflow_2050 | automate | itemlists, htmlextract, gmail | 🔴 High | [2050_workflow_2050.json](workflows/2050_workflow_2050.json) |
| 2054_workflow_2054 | automate | httprequest, schedule, manual | 🔴 High | [2054_workflow_2054.json](workflows/2054_workflow_2054.json) |
| 2058_workflow_2058 | automate | spreadsheetfile, telegram, telegram | 🟡 Medium | [2058_workflow_2058.json](workflows/2058_workflow_2058.json) |
| 2070_workflow_2070 | automate | slack, httprequest, airtable | 🔴 High | [2070_workflow_2070.json](workflows/2070_workflow_2070.json) |
| 2080_workflow_2080 | automate | httprequest, telegram, emailreadimap | 🟡 Medium | [2080_workflow_2080.json](workflows/2080_workflow_2080.json) |
| 2088_workflow_2088 | automate | gmail, schedule, googlesheets | 🟡 Medium | [2088_workflow_2088.json](workflows/2088_workflow_2088.json) |
| 2105_workflow_2105 | automate | respondtowebhook, webhook, manual | 🔴 High | [2105_workflow_2105.json](workflows/2105_workflow_2105.json) |
| 2106_workflow_2106 | automate | gmail, clearbit, form | 🔴 High | [2106_workflow_2106.json](workflows/2106_workflow_2106.json) |
| 2109_workflow_2109 | automate | slack, webhook, clearbit | 🟡 Medium | [2109_workflow_2109.json](workflows/2109_workflow_2109.json) |
| 2110_workflow_2110 | automate | gmail, httprequest, schedule | 🔴 High | [2110_workflow_2110.json](workflows/2110_workflow_2110.json) |
| 2112_workflow_2112 | automate | hubspot, gmail, schedule | 🟡 Medium | [2112_workflow_2112.json](workflows/2112_workflow_2112.json) |
| 2118_workflow_2118 | automate | hubspot, gmail, httprequest | 🟡 Medium | [2118_workflow_2118.json](workflows/2118_workflow_2118.json) |
| 2119_workflow_2119 | automate | slack, httprequest, hunter | 🟡 Medium | [2119_workflow_2119.json](workflows/2119_workflow_2119.json) |
| 2120_workflow_2120 | automate | gmail, httprequest, hunter | 🟡 Medium | [2120_workflow_2120.json](workflows/2120_workflow_2120.json) |
| 2121_workflow_2121 | automate | httprequest, hunter, telegram | 🟡 Medium | [2121_workflow_2121.json](workflows/2121_workflow_2121.json) |
| 2122_workflow_2122 | automate | hubspot, gmail, httprequest | 🔴 High | [2122_workflow_2122.json](workflows/2122_workflow_2122.json) |
| 2124_workflow_2124 | automate | gmail, httprequest, schedule | 🔴 High | [2124_workflow_2124.json](workflows/2124_workflow_2124.json) |
| 2130_workflow_2130 | automate | hubspot, convertkit, clearbit | 🔴 High | [2130_workflow_2130.json](workflows/2130_workflow_2130.json) |
| 2131_workflow_2131 | automate | hubspot, slack, schedule | 🟡 Medium | [2131_workflow_2131.json](workflows/2131_workflow_2131.json) |
| 2135_workflow_2135 | automate | pipedrive, slack, httprequest | 🔴 High | [2135_workflow_2135.json](workflows/2135_workflow_2135.json) |
| 2137_workflow_2137 | automate | gmail, schedule, googlesheets | 🔴 High | [2137_workflow_2137.json](workflows/2137_workflow_2137.json) |
| 2144_workflow_2144 | automate | splitinbatches, gmail, rssfeedread | 🟡 Medium | [2144_workflow_2144.json](workflows/2144_workflow_2144.json) |
| 2146_workflow_2146 | automate | itemlists, gmail, schedule | 🟡 Medium | [2146_workflow_2146.json](workflows/2146_workflow_2146.json) |
| 2150_workflow_2150 | automate | error, slack | 🟢 Low | [2150_workflow_2150.json](workflows/2150_workflow_2150.json) |
| 2157_workflow_2157 | automate | postgres, slack, httprequest | 🔴 High | [2157_workflow_2157.json](workflows/2157_workflow_2157.json) |
| 2159_workflow_2159 | automate | error, telegram | 🟢 Low | [2159_workflow_2159.json](workflows/2159_workflow_2159.json) |
| 2160_workflow_2160 | automate | error, gmail | 🟢 Low | [2160_workflow_2160.json](workflows/2160_workflow_2160.json) |
| 2177_workflow_2177 | automate | schedule, telegram, n8n | 🟡 Medium | [2177_workflow_2177.json](workflows/2177_workflow_2177.json) |
| 2212_workflow_2212 | automate | gmail, httprequest, schedule | 🔴 High | [2212_workflow_2212.json](workflows/2212_workflow_2212.json) |
| 2222_workflow_2222 | automate | slack, webhook, xml | 🟡 Medium | [2222_workflow_2222.json](workflows/2222_workflow_2222.json) |
| 2272_workflow_2272 | automate | postgres, splitinbatches, slack | 🔴 High | [2272_workflow_2272.json](workflows/2272_workflow_2272.json) |
| 2278_workflow_2278 | automate | gmail, httprequest, markdown | 🟡 Medium | [2278_workflow_2278.json](workflows/2278_workflow_2278.json) |
| 2293_workflow_2293 | automate | splitinbatches, slack, webflow | 🔴 High | [2293_workflow_2293.json](workflows/2293_workflow_2293.json) |
| 2312_workflow_2312 | automate | error, gmail, schedule | 🟡 Medium | [2312_workflow_2312.json](workflows/2312_workflow_2312.json) |
| 2327_workflow_2327 | automate | splitinbatches, slack, gmail | 🔴 High | [2327_workflow_2327.json](workflows/2327_workflow_2327.json) |
| 2348_workflow_2348 | automate | gmail, googledrive | 🟢 Low | [2348_workflow_2348.json](workflows/2348_workflow_2348.json) |
| 2353_workflow_2353 | automate | slack, httprequest, schedule | 🟡 Medium | [2353_workflow_2353.json](workflows/2353_workflow_2353.json) |
| 2367_workflow_2367 | automate | slack, httprequest, webhook | 🟡 Medium | [2367_workflow_2367.json](workflows/2367_workflow_2367.json) |
| 2393_workflow_2393 | automate | gmail, httprequest, googledrive | 🔴 High | [2393_workflow_2393.json](workflows/2393_workflow_2393.json) |
| 2402_workflow_2402 | automate | telegram, telegram, googlesheets | 🔴 High | [2402_workflow_2402.json](workflows/2402_workflow_2402.json) |
| 2407_workflow_2407 | automate | gmail, schedule, webhook | 🔴 High | [2407_workflow_2407.json](workflows/2407_workflow_2407.json) |
| 2435_workflow_2435 | automate | slack, httprequest, webhook | 🔴 High | [2435_workflow_2435.json](workflows/2435_workflow_2435.json) |
| 2453_workflow_2453 | automate | supabase, httprequest, telegram | 🔴 High | [2453_workflow_2453.json](workflows/2453_workflow_2453.json) |
| 2455_workflow_2455 | automate | splitinbatches, gmail, httprequest | 🔴 High | [2455_workflow_2455.json](workflows/2455_workflow_2455.json) |
| 2488_workflow_2488 | automate | slack, notion, cron | 🔴 High | [2488_workflow_2488.json](workflows/2488_workflow_2488.json) |
| 2511_workflow_2511 | automate | splitinbatches, slack, httprequest | 🔴 High | [2511_workflow_2511.json](workflows/2511_workflow_2511.json) |
| 2512_workflow_2512 | automate | splitinbatches, slack, httprequest | 🔴 High | [2512_workflow_2512.json](workflows/2512_workflow_2512.json) |
| 2543_workflow_2543 | automate | schedule, wordpress, slack | 🟢 Low | [2543_workflow_2543.json](workflows/2543_workflow_2543.json) |
| 2577_workflow_2577 | automate | slack, httprequest, webhook | 🔴 High | [2577_workflow_2577.json](workflows/2577_workflow_2577.json) |
| 2581_workflow_2581 | automate | slack, form, googlesheets | 🟡 Medium | [2581_workflow_2581.json](workflows/2581_workflow_2581.json) |
| 2585_workflow_2585 | automate | splitinbatches, slack, httprequest | 🔴 High | [2585_workflow_2585.json](workflows/2585_workflow_2585.json) |
| 2676_workflow_2676 | automate | httprequest, webhook, limit | 🔴 High | [2676_workflow_2676.json](workflows/2676_workflow_2676.json) |
| 2677_workflow_2677 | automate | gmail, httprequest, webhook | 🔴 High | [2677_workflow_2677.json](workflows/2677_workflow_2677.json) |
| 2704_workflow_2704 | automate | slack, datetime, schedule | 🔴 High | [2704_workflow_2704.json](workflows/2704_workflow_2704.json) |
| 2708_workflow_2708 | automate | webhook, telegram | 🟡 Medium | [2708_workflow_2708.json](workflows/2708_workflow_2708.json) |
| 2728_workflow_2728 | automate | splitinbatches, slack, httprequest | 🔴 High | [2728_workflow_2728.json](workflows/2728_workflow_2728.json) |
| 2732_workflow_2732 | automate | slack, httprequest, webhook | 🔴 High | [2732_workflow_2732.json](workflows/2732_workflow_2732.json) |
| 27_workflow_27 | automate | telegram, telegram | 🟢 Low | [27_workflow_27.json](workflows/27_workflow_27.json) |
| 2834_workflow_2834 | automate | slack, httprequest, schedule | 🟡 Medium | [2834_workflow_2834.json](workflows/2834_workflow_2834.json) |
| 2853_workflow_2853 | automate | splitinbatches, supabase, comparedatasets | 🔴 High | [2853_workflow_2853.json](workflows/2853_workflow_2853.json) |
| 2966_workflow_2966 | automate | gmail, googledrive | 🟡 Medium | [2966_workflow_2966.json](workflows/2966_workflow_2966.json) |
| 29_workflow_29 | automate | slack, emailsend, typeform | 🟢 Low | [29_workflow_29.json](workflows/29_workflow_29.json) |
| 3034_workflow_3034 | automate | splitinbatches, slack, comparedatasets | 🔴 High | [3034_workflow_3034.json](workflows/3034_workflow_3034.json) |
| 3204_workflow_3204 | automate | googlesheets, gmail, telegram | 🔴 High | [3204_workflow_3204.json](workflows/3204_workflow_3204.json) |
| 3221_workflow_3221 | automate | gmail, gmail, googlesheets | 🔴 High | [3221_workflow_3221.json](workflows/3221_workflow_3221.json) |
| 3251_workflow_3251 | automate | splitinbatches, schedule, mailchimp | 🟡 Medium | [3251_workflow_3251.json](workflows/3251_workflow_3251.json) |
| 3307_workflow_3307 | automate | telegram, telegram, googlesheets | 🔴 High | [3307_workflow_3307.json](workflows/3307_workflow_3307.json) |
| 3366_workflow_3366 | automate | crypto, gmail, httprequest | 🔴 High | [3366_workflow_3366.json](workflows/3366_workflow_3366.json) |
| 3440_workflow_3440 | automate | googlesheets, gmail, n8n-nodes-langchain.code | 🔴 High | [3440_workflow_3440.json](workflows/3440_workflow_3440.json) |
| 3453_workflow_3453 | automate | schedule, microsoftoutlook, mysql | 🟢 Low | [3453_workflow_3453.json](workflows/3453_workflow_3453.json) |
| 3464_workflow_3464 | automate | splitinbatches, gmail, gmail | 🔴 High | [3464_workflow_3464.json](workflows/3464_workflow_3464.json) |
| 353_workflow_353 | automate | pagerduty, jira, webhook | 🟡 Medium | [353_workflow_353.json](workflows/353_workflow_353.json) |
| 3549_workflow_3549 | automate | splitinbatches, gmail, schedule | 🔴 High | [3549_workflow_3549.json](workflows/3549_workflow_3549.json) |
| 354_workflow_354 | automate | pagerduty, webhook, mattermost | 🟢 Low | [354_workflow_354.json](workflows/354_workflow_354.json) |
| 355_workflow_355 | automate | pagerduty, webhook, jira | 🟢 Low | [355_workflow_355.json](workflows/355_workflow_355.json) |
| 359_workflow_359 | automate | error, twilio, mattermost | 🟢 Low | [359_workflow_359.json](workflows/359_workflow_359.json) |
| 3621_workflow_3621 | automate | httprequest, schedule, telegram | 🟡 Medium | [3621_workflow_3621.json](workflows/3621_workflow_3621.json) |
| 3686_workflow_3686 | automate | gmail, telegram, n8n-nodes-langchain.lmchatopenrouter | 🔴 High | [3686_workflow_3686.json](workflows/3686_workflow_3686.json) |
| 368_workflow_368 | automate | freshdesk, telegram, telegram | 🟡 Medium | [368_workflow_368.json](workflows/368_workflow_368.json) |
| 3787_workflow_3787 | automate | splitinbatches, executiondata, discord | 🔴 High | [3787_workflow_3787.json](workflows/3787_workflow_3787.json) |
| 3796_workflow_3796 | automate | splitinbatches, gmail, httprequest | 🔴 High | [3796_workflow_3796.json](workflows/3796_workflow_3796.json) |
| 3923_workflow_3923 | automate | gmail, httprequest, manual | 🔴 High | [3923_workflow_3923.json](workflows/3923_workflow_3923.json) |
| 3937_workflow_3937 | automate | whatsapp, whatsapp | 🟡 Medium | [3937_workflow_3937.json](workflows/3937_workflow_3937.json) |
| 3954_workflow_3954 | automate | gmail, httprequest, form | 🔴 High | [3954_workflow_3954.json](workflows/3954_workflow_3954.json) |
| 3979_workflow_3979 | automate | supabase, itemlists, gmail | 🔴 High | [3979_workflow_3979.json](workflows/3979_workflow_3979.json) |
| 398_workflow_398 | automate | slack, emailsend, typeform | 🟢 Low | [398_workflow_398.json](workflows/398_workflow_398.json) |
| 404_workflow_404 | automate | slack, emailsend, typeform | 🟢 Low | [404_workflow_404.json](workflows/404_workflow_404.json) |
| 471_workflow_471 | automate | httprequest, cron, discord | 🟡 Medium | [471_workflow_471.json](workflows/471_workflow_471.json) |
| 4_workflow_4 | automate | slack, github | 🟢 Low | [4_workflow_4.json](workflows/4_workflow_4.json) |
| 516_workflow_516 | automate | mailchimp | 🟢 Low | [516_workflow_516.json](workflows/516_workflow_516.json) |
| 613_workflow_613 | automate | webhook, mattermost | 🟢 Low | [613_workflow_613.json](workflows/613_workflow_613.json) |
| 632_workflow_632 | automate | spreadsheetfile, slack, emailsend | 🟡 Medium | [632_workflow_632.json](workflows/632_workflow_632.json) |
| 680_workflow_680 | automate | manual, microsoftteams | 🟢 Low | [680_workflow_680.json](workflows/680_workflow_680.json) |
| 696_workflow_696 | automate | error, gmail | 🟢 Low | [696_workflow_696.json](workflows/696_workflow_696.json) |
| 730_workflow_730 | automate | gmail, googlecalendar, typeform | 🟡 Medium | [730_workflow_730.json](workflows/730_workflow_730.json) |
| 731_workflow_731 | automate | googlesheets, mattermost, cron | 🟢 Low | [731_workflow_731.json](workflows/731_workflow_731.json) |
| 772_workflow_772 | automate | splitinbatches, manual, telegram | 🟢 Low | [772_workflow_772.json](workflows/772_workflow_772.json) |
| 864_workflow_864 | automate | googlesheets, interval, mattermost | 🟢 Low | [864_workflow_864.json](workflows/864_workflow_864.json) |
| 916_workflow_916 | automate | typeform, slack, airtable | 🟢 Low | [916_workflow_916.json](workflows/916_workflow_916.json) |
| 965_workflow_965 | automate | awscomprehend, mattermost, typeform | 🟢 Low | [965_workflow_965.json](workflows/965_workflow_965.json) |
| 984_workflow_984 | automate | lemlist, mattermost | 🟢 Low | [984_workflow_984.json](workflows/984_workflow_984.json) |
| AjD7Xo4vjbBvBb93_workflow_AjD7Xo4vjbBvBb93 | automate | trello, gmail, rssfeedread | 🔴 High | [AjD7Xo4vjbBvBb93_workflow_AjD7Xo4vjbBvBb93.json](workflows/AjD7Xo4vjbBvBb93_workflow_AjD7Xo4vjbBvBb93.json) |
| Automate Your Customer Service With WhatsApp Business Cloud & Asana | automate | whatsapp, asana, form | 🟡 Medium | [lWfWe93aNGuNPLBz_Automate_Your_Customer_Service_With_WhatsApp_Business_Cloud_&_Asana.json](workflows/lWfWe93aNGuNPLBz_Automate_Your_Customer_Service_With_WhatsApp_Business_Cloud_&_Asana.json) |
| BillBot | automate | httprequest, telegram, telegram | 🟡 Medium | [200_BillBot.json](workflows/200_BillBot.json) |
| Bitrix24 Chatbot Application Workflow example with Webhook Integration | automate | httprequest, webhook, respondtowebhook | 🔴 High | [Bitrix24 Chatbot Application Workflow example with Webhook Integration.json](workflows/Bitrix24 Chatbot Application Workflow example with Webhook Integration.json) |
| Bitrix24 Chatbot Application Workflow example with Webhook Integration | automate | httprequest, webhook, respondtowebhook | 🔴 High | [cmGsNvW9bEORABdo_Bitrix24_Chatbot_Application_Workflow_example_with_Webhook_Integration.json](workflows/cmGsNvW9bEORABdo_Bitrix24_Chatbot_Application_Workflow_example_with_Webhook_Integration.json) |
| CV Evaluation - Error Handling | automate | error, gmail, html | 🔴 High | [vnhhf9aNsw0kzdBV_CV_Evaluation_-_Error_Handling.json](workflows/vnhhf9aNsw0kzdBV_CV_Evaluation_-_Error_Handling.json) |
| Coffee Bot (Mattermost) | automate | cron, googlecalendar, mattermost | 🟢 Low | [7_Coffee_Bot_(Mattermost).json](workflows/7_Coffee_Bot_(Mattermost).json) |
| DSP Certificate w/ Google Forms | automate | googleslides, gmail, googledrive | 🔴 High | [2qIFnWXdHJJs4oBk_DSP_Certificate_w__Google_Forms.json](workflows/2qIFnWXdHJJs4oBk_DSP_Certificate_w__Google_Forms.json) |
| Daylight Saving Time Notification | automate | slack, datetime, emailsend | 🟡 Medium | [JIegnKLVXTkkTzfO_Daylight_Saving_Time_Notification.json](workflows/JIegnKLVXTkkTzfO_Daylight_Saving_Time_Notification.json) |
| DeepSeek v3.1 | automate | n8n-nodes-langchain.lmchatdeepseek, notion, n8n-nodes-langchain.agent | 🟡 Medium | [7eyNPahKcCuqK39V_DeepSeek_v3.1.json](workflows/7eyNPahKcCuqK39V_DeepSeek_v3.1.json) |
| Detect toxic language in Telegram messages | automate | N/A | 🟢 Low | [Detect toxic language in Telegram messages.json](workflows/Detect toxic language in Telegram messages.json) |
| Discord Intro | automate | manual, discord | 🟢 Low | [2_Discord_Intro.json](workflows/2_Discord_Intro.json) |
| Discord MCP Server | automate | httprequest, discord, n8n-nodes-langchain.mcp | 🟡 Medium | [ly8aZhPk5ZI8uB0Y_Discord_MCP_Server.json](workflows/ly8aZhPk5ZI8uB0Y_Discord_MCP_Server.json) |
| ETL pipeline | automate | postgres, slack, googlecloudnaturallanguage | 🟡 Medium | [6_ETL_pipeline.json](workflows/6_ETL_pipeline.json) |
| ETL pipeline | automate | postgres, slack, googlecloudnaturallanguage | 🟡 Medium | [ETL pipeline for text processing.json](workflows/ETL pipeline for text processing.json) |
| Error Handler send Telegram | automate | error, telegram | 🟢 Low | [ozo5jlbwPHgaMnVt_Error_Handler_send_Telegram.json](workflows/ozo5jlbwPHgaMnVt_Error_Handler_send_Telegram.json) |
| Extranet Releases | automate | slack, github | 🟢 Low | [5ec2322573f7590007802e1f_Extranet_Releases.json](workflows/5ec2322573f7590007802e1f_Extranet_Releases.json) |
| GROQ LLAVA V1.5 7B | automate | httprequest, telegram, telegram | 🟡 Medium | [aDPpPIaeM7zfUCdJ_GROQ_LLAVA_V1.5_7B.json](workflows/aDPpPIaeM7zfUCdJ_GROQ_LLAVA_V1.5_7B.json) |
| Gender Inclusive Language | automate | webhook, mattermost | 🟢 Low | [18_Gender_Inclusive_Language.json](workflows/18_Gender_Inclusive_Language.json) |
| Google Calendar to Slack Status & Philips Hue | automate | slack, httprequest, googlecalendar | 🟡 Medium | [118_Google_Calendar_to_Slack_Status_&_Philips_Hue.json](workflows/118_Google_Calendar_to_Slack_Status_&_Philips_Hue.json) |
| Google calendar to Outlook | automate | googlecalendar, microsoftoutlook | 🟢 Low | [0HVA2TOmkdNpH5DP_Google_calendar_to_Outlook.json](workflows/0HVA2TOmkdNpH5DP_Google_calendar_to_Outlook.json) |
| Gumroad sale trigger | automate | mailerlite, httprequest, googlesheets | 🟡 Medium | [06v55r6E13Wfvo66_Gumroad_sale_trigger.json](workflows/06v55r6E13Wfvo66_Gumroad_sale_trigger.json) |
| Keep discord clean | automate | splitinbatches, schedule, discord | 🟡 Medium | [QCbb7Bm12gDIH0mI_Keep_discord_clean.json](workflows/QCbb7Bm12gDIH0mI_Keep_discord_clean.json) |
| Lead Qualification with BatchData | automate | slack, httprequest, webhook | 🔴 High | [0uon02fOzPkLcG6G_Lead_Qualification_with_BatchData.json](workflows/0uon02fOzPkLcG6G_Lead_Qualification_with_BatchData.json) |
| Linkedin Automation | automate | httprequest, linkedin, schedule | 🔴 High | [yF1HNe2ucaE81fNl_Linkedin_Automation.json](workflows/yF1HNe2ucaE81fNl_Linkedin_Automation.json) |
| MCP Client with Brave and Telegram | automate | telegram, telegram | 🟡 Medium | [52pBJt8swWgtdY54_MCP_Client_with_Brave_and_Telegram.json](workflows/52pBJt8swWgtdY54_MCP_Client_with_Brave_and_Telegram.json) |
| Mattermost Webhook | automate | webhook, httprequest, mattermost | 🟢 Low | [13_Mattermost_Webhook.json](workflows/13_Mattermost_Webhook.json) |
| Meeting booked - to newsletter and CRM | automate | httprequest, cal, telegram | 🟡 Medium | [xe9sXQUc7yW8P8im_Meeting_booked_-_to_newsletter_and_CRM.json](workflows/xe9sXQUc7yW8P8im_Meeting_booked_-_to_newsletter_and_CRM.json) |
| MiniBear Webhook | automate | n8n-nodes-langchain.outputparserstructured, httprequest, webhook | 🔴 High | [HbjZ9cBPgDdnIRjG_MiniBear_Webhook.json](workflows/HbjZ9cBPgDdnIRjG_MiniBear_Webhook.json) |
| My workflow | automate | gmail, hunter, googlesheets | 🟡 Medium | [yYjRbTWULZuNLXM0_My_workflow.json](workflows/yYjRbTWULZuNLXM0_My_workflow.json) |
| My workflow 3 | automate | gmail, httprequest, cron | 🟡 Medium | [jbTm6O9bLBMm6RWy_My_workflow_3.json](workflows/jbTm6O9bLBMm6RWy_My_workflow_3.json) |
| My workflow 4 | automate | gmail, rssfeedread, schedule | 🟡 Medium | [Glb4VNoQI44GT0p9_My_workflow_4.json](workflows/Glb4VNoQI44GT0p9_My_workflow_4.json) |
| My workflow 4 | automate | emailsend, httprequest, webhook | 🟡 Medium | [mW6b4dMHkIDfnaIj_My_workflow_4.json](workflows/mW6b4dMHkIDfnaIj_My_workflow_4.json) |
| N8N Español - BOT | automate | telegram, telegram | 🟢 Low | [27_N8N_Español_-_BOT.json](workflows/27_N8N_Español_-_BOT.json) |
| N8N Español - NocodeBot | automate | httprequest, executecommand, telegram | 🟡 Medium | [30_N8N_Español_-_NocodeBot.json](workflows/30_N8N_Español_-_NocodeBot.json) |
| New WooCommerce Product to Twitter and Telegram | automate | woocommerce, telegram, twitter | 🟢 Low | [85_New_WooCommerce_Product_to_Twitter_and_Telegram.json](workflows/85_New_WooCommerce_Product_to_Twitter_and_Telegram.json) |
| New WooCommerce order to Slack | automate | slack, woocommerce | 🟢 Low | [81_New_WooCommerce_order_to_Slack.json](workflows/81_New_WooCommerce_order_to_Slack.json) |
| New WooCommerce product to Slack | automate | slack, woocommerce | 🟢 Low | [80_New_WooCommerce_product_to_Slack.json](workflows/80_New_WooCommerce_product_to_Slack.json) |
| New WooCommerce refund to Slack | automate | slack, woocommerce | 🟢 Low | [82_New_WooCommerce_refund_to_Slack.json](workflows/82_New_WooCommerce_refund_to_Slack.json) |
| Onfleet Driver signup message in Slack | automate | onfleet, slack | 🟢 Low | [14_Onfleet_Driver_signup_message_in_Slack.json](workflows/14_Onfleet_Driver_signup_message_in_Slack.json) |
| Orlen | automate | slack, gmail, manual | 🟡 Medium | [3_Orlen.json](workflows/3_Orlen.json) |
| Phishing_analysis__URLScan_io_and_Virustotal_ | automate | splitinbatches, slack, httprequest | 🔴 High | [8EmNhftXznAGV3dR_Phishing_analysis__URLScan_io_and_Virustotal_.json](workflows/8EmNhftXznAGV3dR_Phishing_analysis__URLScan_io_and_Virustotal_.json) |
| Post RSS feed items from yesterday to Slack | automate | slack, datetime, rssfeedread | 🟡 Medium | [89_Post_RSS_feed_items_from_yesterday_to_Slack.json](workflows/89_Post_RSS_feed_items_from_yesterday_to_Slack.json) |
| Post a message to a channel in RocketChat | automate | rocketchat, manual | 🟢 Low | [90_Post_a_message_to_a_channel_in_RocketChat.json](workflows/90_Post_a_message_to_a_channel_in_RocketChat.json) |
| Post new Google Calendar events to Telegram | automate | googlecalendar, telegram | 🟢 Low | [CoYwFuZTq5kUuiba_Post_new_Google_Calendar_events_to_Telegram.json](workflows/CoYwFuZTq5kUuiba_Post_new_Google_Calendar_events_to_Telegram.json) |
| RSS to Telegram | automate | rssfeedread, telegram, cron | 🟡 Medium | [2_RSS_to_Telegram.json](workflows/2_RSS_to_Telegram.json) |
| Real Estate Market Scanning | automate | slack, emailsend, httprequest | 🔴 High | [WUFuYk56jNNpjfZm_Real_Estate_Market_Scanning.json](workflows/WUFuYk56jNNpjfZm_Real_Estate_Market_Scanning.json) |
| Receive messages for a MQTT queue | automate | mqtt | 🟢 Low | [51_Receive_messages_for_a_MQTT_queue.json](workflows/51_Receive_messages_for_a_MQTT_queue.json) |
| Receive messages for an ActiveMQ queue via AMQP Trigger | automate | amqp | 🟢 Low | [135_Receive_messages_for_an_ActiveMQ_queue_via_AMQP_Trigger.json](workflows/135_Receive_messages_for_an_ActiveMQ_queue_via_AMQP_Trigger.json) |
| Receive messages from a queue via RabbitMQ and send an SMS | automate | rabbitmq, vonage | 🟢 Low | [186_Receive_messages_from_a_queue_via_RabbitMQ_and_send_an_SMS.json](workflows/186_Receive_messages_from_a_queue_via_RabbitMQ_and_send_an_SMS.json) |
| Receive messages from a topic and send an SMS | automate | vonage, kafka | 🟢 Low | [166_Receive_messages_from_a_topic_and_send_an_SMS.json](workflows/166_Receive_messages_from_a_topic_and_send_an_SMS.json) |
| Save new Files received on Telegram to Google Drive | automate | telegram, googledrive | 🟢 Low | [a4GTp998ENMMfuqK_Save_new_Files_received_on_Telegram_to_Google_Drive.json](workflows/a4GTp998ENMMfuqK_Save_new_Files_received_on_Telegram_to_Google_Drive.json) |
| Send Discord message from Webflow form submission | automate | webflow, discord | 🟡 Medium | [cGTxHYV93kS71hLL_Send_Discord_message_from_Webflow_form_submission.json](workflows/cGTxHYV93kS71hLL_Send_Discord_message_from_Webflow_form_submission.json) |
| Send Slack message from Webflow form submission | automate | slack, webflow | 🟡 Medium | [pmJUJj7FAnrOS6Jc_Send_Slack_message_from_Webflow_form_submission.json](workflows/pmJUJj7FAnrOS6Jc_Send_Slack_message_from_Webflow_form_submission.json) |
| Send a message on Twake | automate | twake, manual | 🟢 Low | [1_Send_a_message_on_Twake.json](workflows/1_Send_a_message_on_Twake.json) |
| Send a private message on Zulip | automate | zulip, manual | 🟢 Low | [126_Send_a_private_message_on_Zulip.json](workflows/126_Send_a_private_message_on_Zulip.json) |
| Send a random recipe once a day to Telegram | automate | cron, httprequest, telegram | 🔴 High | [Send a random recipe once a day to Telegram.json](workflows/Send a random recipe once a day to Telegram.json) |
| Send financial metrics monthly to Mattermost | automate | profitwell, mattermost, cron | 🟢 Low | [146_Send_financial_metrics_monthly_to_Mattermost.json](workflows/146_Send_financial_metrics_monthly_to_Mattermost.json) |
| Sending an SMS using sms77 | automate | manual, sms77 | 🟢 Low | [92_Sending_an_SMS_using_sms77.json](workflows/92_Sending_an_SMS_using_sms77.json) |
| Sending an SMS with MessageBird | automate | messagebird, manual | 🟢 Low | [85_Sending_an_SMS_with_MessageBird.json](workflows/85_Sending_an_SMS_with_MessageBird.json) |
| Slack-GitHub User Info | automate | webhook, graphql, slack | 🟢 Low | [5_Slack-GitHub_User_Info.json](workflows/5_Slack-GitHub_User_Info.json) |
| Standup Bot - Worker | automate | cron, httprequest, webhook | 🔴 High | [114_Standup_Bot_-_Worker.json](workflows/114_Standup_Bot_-_Worker.json) |
| StatsInstagram | automate | datetime, cron, googlesheets | 🟢 Low | [3_StatsInstagram.json](workflows/3_StatsInstagram.json) |
| Suspicious_login_detection | automate | postgres, slack, gmail | 🔴 High | [xQHiKDTkezDY5lFu_Suspicious_login_detection.json](workflows/xQHiKDTkezDY5lFu_Suspicious_login_detection.json) |
| Telegram Weather Workflow | automate | openweathermap, telegram, telegram | 🟢 Low | [2_Telegram_Weather_Workflow.json](workflows/2_Telegram_Weather_Workflow.json) |
| Telegram echo-bot | automate | telegram, telegram | 🟢 Low | [o8HjmolfMilbaEkk_Telegram_echo-bot.json](workflows/o8HjmolfMilbaEkk_Telegram_echo-bot.json) |
| Twitter notifications | automate | cron, twitter, mattermost | 🟢 Low | [1_Twitter_notifications.json](workflows/1_Twitter_notifications.json) |
| Weather via Slack | automate | webhook, httprequest, slack | 🟢 Low | [B6UHILmjPWa7ViQ4_Weather_via_Slack.json](workflows/B6UHILmjPWa7ViQ4_Weather_via_Slack.json) |
| WhatsApp business bot | automate | splitinbatches, whatsapp, schedule | 🔴 High | [NzoLNV2FbS4eurJ7_WhatsApp_business_bot.json](workflows/NzoLNV2FbS4eurJ7_WhatsApp_business_bot.json) |
| WhatsApp starter workflow | automate | webhook, whatsapp, respondtowebhook | 🟡 Medium | [yxv7OYbDEnqsqfa9_WhatsApp_starter_workflow.json](workflows/yxv7OYbDEnqsqfa9_WhatsApp_starter_workflow.json) |
| Zendesk-to-slack | automate | slack, manual, zendesk | 🟢 Low | [23_Zendesk-to-slack.json](workflows/23_Zendesk-to-slack.json) |
| bash-dash telegram | automate | webhook, telegram | 🟢 Low | [5_bash-dash_telegram.json](workflows/5_bash-dash_telegram.json) |
| cheems | automate | discord, cron | 🟢 Low | [1_cheems.json](workflows/1_cheems.json) |
| line message api demo | automate | httprequest, webhook, manual | 🟡 Medium | [a5tCsfMzJPd8WDUj_line_message_api_demo.json](workflows/a5tCsfMzJPd8WDUj_line_message_api_demo.json) |
| rss-telegram | automate | splitinbatches, rssfeedread, manual | 🔴 High | [3_rss-telegram.json](workflows/3_rss-telegram.json) |
| send file to kindle through telegram bot | automate | microsoftoutlook, telegram, telegram | 🟡 Medium | [okMME97B70fXzK5U_send_file_to_kindle_through_telegram_bot.json](workflows/okMME97B70fXzK5U_send_file_to_kindle_through_telegram_bot.json) |
| 外送記帳 | automate | splitinbatches, slack, gmail | 🟡 Medium | [dDInVHNAfSedBUCb_外送記帳.json](workflows/dDInVHNAfSedBUCb_外送記帳.json) |
| ✨😃Automated Workflow Backups to Google Drive | backup | splitinbatches, schedule, manual | 🔴 High | [o4sdVtTrkuZXDATf_✨😃Automated_Workflow_Backups_to_Google_Drive.json](workflows/o4sdVtTrkuZXDATf_✨😃Automated_Workflow_Backups_to_Google_Drive.json) |
| 2. Add Beehiiv newsletter subscribers from Gumroad sales | create | httprequest, telegram, googlesheets | 🟡 Medium | [W1xEzKKEd1qV2D7V_2._Add_Beehiiv_newsletter_subscribers_from_Gumroad_sales.json](workflows/W1xEzKKEd1qV2D7V_2._Add_Beehiiv_newsletter_subscribers_from_Gumroad_sales.json) |
| Add positive feedback messages to a table in Notion | create | slack, googlecloudnaturallanguage, trello | 🟡 Medium | [Add positive feedback messages to a table in Notion.json](workflows/Add positive feedback messages to a table in Notion.json) |
| Add subscriber to form, create tag and subscriber to the tag | create | manual, convertkit | 🟢 Low | [25_Add_subscriber_to_form,_create_tag_and_subscriber_to_the_tag.json](workflows/25_Add_subscriber_to_form,_create_tag_and_subscriber_to_the_tag.json) |
| Addon for Workflow Nodes Update Check Template | create | gmail, n8n, executeworkflow | 🔴 High | [xlMrGt0c1eFi4J1U_Addon_for_Workflow_Nodes_Update_Check_Template.json](workflows/xlMrGt0c1eFi4J1U_Addon_for_Workflow_Nodes_Update_Check_Template.json) |
| Create a channel, add a member, and post a message to the channel | create | manual, mattermost | 🟢 Low | [178_Create_a_channel,_add_a_member,_and_post_a_message_to_the_channel.json](workflows/178_Create_a_channel,_add_a_member,_and_post_a_message_to_the_channel.json) |
| Create a room, invite members from a different room, and send a message in the room we created | create | matrix, manual | 🟡 Medium | [83_Create_a_room,_invite_members_from_a_different_room,_and_send_a_message_in_the_room_we_created.json](workflows/83_Create_a_room,_invite_members_from_a_different_room,_and_send_a_message_in_the_room_we_created.json) |
| Create a screenshot of a website and send it to a telegram channel | create | uproc, manual, telegram | 🟢 Low | [191_Create_a_screenshot_of_a_website_and_send_it_to_a_telegram_channel.json](workflows/191_Create_a_screenshot_of_a_website_and_send_it_to_a_telegram_channel.json) |
| Create and update a channel, and send a message on Twist | create | manual, twist | 🟢 Low | [173_Create_and_update_a_channel,_and_send_a_message_on_Twist.json](workflows/173_Create_and_update_a_channel,_and_send_a_message_on_Twist.json) |
| Create, add an attachment, and send a draft using the Microsoft Outlook node | create | microsoftoutlook, httprequest, manual | 🟢 Low | [193_Create,_add_an_attachment,_and_send_a_draft_using_the_Microsoft_Outlook_node.json](workflows/193_Create,_add_an_attachment,_and_send_a_draft_using_the_Microsoft_Outlook_node.json) |
| Receive updates when a subscriber is added through a form in ConvertKit | create | convertkit | 🟢 Low | [28_Receive_updates_when_a_subscriber_is_added_through_a_form_in_ConvertKit.json](workflows/28_Receive_updates_when_a_subscriber_is_added_through_a_form_in_ConvertKit.json) |
| Send a message on Mattermost when an order is created in WooCommerce | create | woocommerce, mattermost | 🟢 Low | [188_Send_a_message_on_Mattermost_when_an_order_is_created_in_WooCommerce.json](workflows/188_Send_a_message_on_Mattermost_when_an_order_is_created_in_WooCommerce.json) |
| Create a channel, invite users to the channel, post a message, and upload a file | create_contact | slack, httprequest, manual | 🟢 Low | [164_Create_a_channel,_invite_users_to_the_channel,_post_a_message,_and_upload_a_file.json](workflows/164_Create_a_channel,_invite_users_to_the_channel,_post_a_message,_and_upload_a_file.json) |
| Create, update and get a contact using the SendGrid node | create_contact | sendgrid, manual | 🟢 Low | [209_Create,_update_and_get_a_contact_using_the_SendGrid_node.json](workflows/209_Create,_update_and_get_a_contact_using_the_SendGrid_node.json) |
| FetchGithubIssues | extract | schedule, telegram, github | 🟡 Medium | [okjjim5PVb2dZUgg_FetchGithubIssues.json](workflows/okjjim5PVb2dZUgg_FetchGithubIssues.json) |
| Scrape Twitter for mentions of company | extract | slack, datetime, cron | 🟡 Medium | [95_Scrape_Twitter_for_mentions_of_company.json](workflows/95_Scrape_Twitter_for_mentions_of_company.json) |
| Generate google meet links in slack | generate | webhook, slack, googlecalendar | 🟡 Medium | [O2R3U22TB968fWUo_Generate_google_meet_links_in_slack.json](workflows/O2R3U22TB968fWUo_Generate_google_meet_links_in_slack.json) |
| Monitor Competitor Pricing | monitor | slack, airtop, manual | 🟡 Medium | [XY0cZQwrhzOkisSt_Monitor_Competitor_Pricing.json](workflows/XY0cZQwrhzOkisSt_Monitor_Competitor_Pricing.json) |
| Monitor ProductHunt | monitor | slack, airtop, schedule | 🟢 Low | [fvYgcG9s1pqP5cQ6_Monitor_ProductHunt.json](workflows/fvYgcG9s1pqP5cQ6_Monitor_ProductHunt.json) |
| Monitor USDT ERC-20 Wallet Balance with Etherscan and Telegram Notifications | monitor | cron, httprequest, telegram | 🟡 Medium | [AlEVIPHR3dMJkYWt_Monitor_USDT_ERC-20_Wallet_Balance_with_Etherscan_and_Telegram_Notifications.json](workflows/AlEVIPHR3dMJkYWt_Monitor_USDT_ERC-20_Wallet_Balance_with_Etherscan_and_Telegram_Notifications.json) |
| Monitor_security_advisories | monitor | n8ntrainingcustomerdatastore, gmail, rssfeedread | 🔴 High | [YSjQ7TVCNY9v1F2A_Monitor_security_advisories.json](workflows/YSjQ7TVCNY9v1F2A_Monitor_security_advisories.json) |
| N_01_Simple_Lead_Tracker_Automation_v4 | monitor | hubspot, slack, gmail | 🔴 High | [hmgR6wOkuqrn5y4Y_N_01_Simple_Lead_Tracker_Automation_v4.json](workflows/hmgR6wOkuqrn5y4Y_N_01_Simple_Lead_Tracker_Automation_v4.json) |
| Web Server Monitor. | monitor | gmail, httprequest, schedule | 🟡 Medium | [pcLi17oUJK9pSaee_Web_Server_Monitor..json](workflows/pcLi17oUJK9pSaee_Web_Server_Monitor..json) |
| n8n Community Topic Tracker by Keyword | monitor | slack, emailsend, httprequest | 🟡 Medium | [R6tFG45dQydBz63e_n8n_Community_Topic_Tracker_by_Keyword.json](workflows/R6tFG45dQydBz63e_n8n_Community_Topic_Tracker_by_Keyword.json) |
| Create_Unique_Jira_tickets_from_Splunk_alerts | notify | jira, webhook | 🟡 Medium | [uD31xU0VYjogxWoY_Create_Unique_Jira_tickets_from_Splunk_alerts.json](workflows/uD31xU0VYjogxWoY_Create_Unique_Jira_tickets_from_Splunk_alerts.json) |
| Monitoring and alerting | notify | postgres, twilio, cron | 🟢 Low | [34_Monitoring_and_alerting.json](workflows/34_Monitoring_and_alerting.json) |
| New Ticket Alerts to Teams | notify | httprequest, schedule, microsoftteams | 🟡 Medium | [0H2mo5k35e0nzMEE_New_Ticket_Alerts_to_Teams.json](workflows/0H2mo5k35e0nzMEE_New_Ticket_Alerts_to_Teams.json) |
| On new Stripe Invoice Payment update Hubspot and notify the team in Slack | notify | stripe, hubspot, slack | 🟡 Medium | [100_On_new_Stripe_Invoice_Payment_update_Hubspot_and_notify_the_team_in_Slack.json](workflows/100_On_new_Stripe_Invoice_Payment_update_Hubspot_and_notify_the_team_in_Slack.json) |
| SIGNL4 Alert | notify | movebinarydata, cron, signl4 | 🟡 Medium | [2_SIGNL4_Alert.json](workflows/2_SIGNL4_Alert.json) |
| SSL Expiry Alert | notify | gmail, httprequest, schedule | 🟡 Medium | [Qj1307oyBx1hZJy5_SSL_Expiry_Alert.json](workflows/Qj1307oyBx1hZJy5_SSL_Expiry_Alert.json) |
| Send Telegram Alerts for New WooCommerce Orders | notify | webhook, telegram | 🟡 Medium | [JMfwq2Xn60pWz2Hy_Send_Telegram_Alerts_for_New_WooCommerce_Orders.json](workflows/JMfwq2Xn60pWz2Hy_Send_Telegram_Alerts_for_New_WooCommerce_Orders.json) |
| Template - SSL Expiry Alert System | notify | gmail, httprequest, schedule | 🔴 High | [JH0OhDnJCwPxBJZX_Template_-_SSL_Expiry_Alert_System.json](workflows/JH0OhDnJCwPxBJZX_Template_-_SSL_Expiry_Alert_System.json) |
| Get PDF with JSReport | read | gmail, httprequest, form | 🟢 Low | [i8nBvPOtFYWk5eoq_Get_PDF_with_JSReport.json](workflows/i8nBvPOtFYWk5eoq_Get_PDF_with_JSReport.json) |
| Get SSL Certificate | read | uproc, functionitem, manual | 🟢 Low | [110_Get_SSL_Certificate.json](workflows/110_Get_SSL_Certificate.json) |
| Save Telegram reply to journal spreadsheet | read | functionitem, googlesheets, telegram | 🟢 Low | [4_Save_Telegram_reply_to_journal_spreadsheet.json](workflows/4_Save_Telegram_reply_to_journal_spreadsheet.json) |
| Automate Google Analytics Reporting - AlexK1919 | report | gmail, googleanalytics, schedule | 🔴 High | [21IdmArlNT9LlaFf_Automate_Google_Analytics_Reporting_-_AlexK1919.json](workflows/21IdmArlNT9LlaFf_Automate_Google_Analytics_Reporting_-_AlexK1919.json) |
| Parse DMARC reports | report | slack, datetime, emailsend | 🔴 High | [ATxZ5QYhdJq9mZDO_Parse_DMARC_reports.json](workflows/ATxZ5QYhdJq9mZDO_Parse_DMARC_reports.json) |
| Check To Do on Notion and send message on Slack | send | slack, notion, cron | 🟡 Medium | [331_Check_To_Do_on_Notion_and_send_message_on_Slack.json](workflows/331_Check_To_Do_on_Notion_and_send_message_on_Slack.json) |
| [hiroshidigital.com] Send Message In Larksuite | send | httprequest, manual | 🟢 Low | [IjQRdNu2ItwNnGL2_[hiroshidigital.com]_Send_Message_In_Larksuite.json](workflows/IjQRdNu2ItwNnGL2_[hiroshidigital.com]_Send_Message_In_Larksuite.json) |
| Linear Project Status and End Date to Productboard feature Sync | sync | linear, slack, httprequest | 🔴 High | [2578_Linear_Project_Status_and_End_Date_to_Productboard_feature_Sync.json](workflows/2578_Linear_Project_Status_and_End_Date_to_Productboard_feature_Sync.json) |
| Realtime Notion Todoist 2-way Sync Template | sync | httprequest, comparedatasets, redis | 🔴 High | [k9abwUyVzl7OCsAl_Realtime_Notion_Todoist_2-way_Sync_Template.json](workflows/k9abwUyVzl7OCsAl_Realtime_Notion_Todoist_2-way_Sync_Template.json) |
| Syncro Alert to OpsGenie | sync | httprequest, webhook | 🟡 Medium | [117_Syncro_Alert_to_OpsGenie.json](workflows/117_Syncro_Alert_to_OpsGenie.json) |
| Import Productboard Notes, Companies and Features into Snowflake | transfer | splitinbatches, slack, httprequest | 🔴 High | [2576_Import_Productboard_Notes,_Companies_and_Features_into_Snowflake.json](workflows/2576_Import_Productboard_Notes,_Companies_and_Features_into_Snowflake.json) |
| Get event triggered notifications / updates on preferred messaging channels with TwentyCRM | update | slack, gmail, webhook | 🟡 Medium | [1dnr1k4MAVbDiBmO_Get_event_triggered_notifications___updates_on_preferred_messaging_channels_with_TwentyCRM.json](workflows/1dnr1k4MAVbDiBmO_Get_event_triggered_notifications___updates_on_preferred_messaging_channels_with_TwentyCRM.json) |
| Receive a Mattermost message when a user updates their profile on Facebook | update | facebook, mattermost | 🟢 Low | [131_Receive_a_Mattermost_message_when_a_user_updates_their_profile_on_Facebook.json](workflows/131_Receive_a_Mattermost_message_when_a_user_updates_their_profile_on_Facebook.json) |
| n8n update | update | ssh, httprequest, schedule | 🔴 High | [PVBUCGQUOiOrIfli_n8n_update.json](workflows/PVBUCGQUOiOrIfli_n8n_update.json) |
| Telegram Tron Wallet Blacklist Checker | validate | httprequest, telegram, telegram | 🟡 Medium | [RMxcTgpFGpE3RdLZ_Telegram_Tron_Wallet_Blacklist_Checker.json](workflows/RMxcTgpFGpE3RdLZ_Telegram_Tron_Wallet_Blacklist_Checker.json) |
| Website check | validate | cron, httprequest, discord | 🟢 Low | [1_Website_check.json](workflows/1_Website_check.json) |
| n8n_check | validate | awsses, rssfeedread, manual | 🟡 Medium | [33_n8n_check.json](workflows/33_n8n_check.json) |

## DATA

*204 workflows in this category*

| Workflow Name | Business Function | Key Integrations | Complexity | File |
|---------------|-------------------|------------------|------------|------|
| 1055_workflow_1055 | automate | mailcheck, airtable | 🟢 Low | [1055_workflow_1055.json](workflows/1055_workflow_1055.json) |
| 1076_workflow_1076 | automate | googlesheets, webhook | 🟢 Low | [1076_workflow_1076.json](workflows/1076_workflow_1076.json) |
| 1088_workflow_1088 | automate | calendly, notion | 🟢 Low | [1088_workflow_1088.json](workflows/1088_workflow_1088.json) |
| 1093_workflow_1093 | automate | crypto, webhook, airtable | 🔴 High | [1093_workflow_1093.json](workflows/1093_workflow_1093.json) |
| 1107_workflow_1107 | automate | calendly, humanticai, notion | 🟢 Low | [1107_workflow_1107.json](workflows/1107_workflow_1107.json) |
| 1110_workflow_1110 | automate | htmlextract, httprequest, notion | 🟡 Medium | [1110_workflow_1110.json](workflows/1110_workflow_1110.json) |
| 1122_workflow_1122 | automate | interval, notion, notion | 🟡 Medium | [1122_workflow_1122.json](workflows/1122_workflow_1122.json) |
| 11_workflow_11 | automate | spreadsheetfile, googlesheets, interval | 🟢 Low | [11_workflow_11.json](workflows/11_workflow_11.json) |
| 1236_workflow_1236 | automate | webhook, airtable, redis | 🟡 Medium | [1236_workflow_1236.json](workflows/1236_workflow_1236.json) |
| 1253_workflow_1253 | automate | airtable, netlify | 🟢 Low | [1253_workflow_1253.json](workflows/1253_workflow_1253.json) |
| 1304_workflow_1304 | automate | googlesheets, dropcontact, lemlist | 🟢 Low | [1304_workflow_1304.json](workflows/1304_workflow_1304.json) |
| 1325_workflow_1325 | automate | dropcontact, calendly, notion | 🟢 Low | [1325_workflow_1325.json](workflows/1325_workflow_1325.json) |
| 1363_workflow_1363 | automate | postgres, httprequest, webhook | 🟡 Medium | [1363_workflow_1363.json](workflows/1363_workflow_1363.json) |
| 1373_workflow_1373 | automate | notion, webhook | 🟡 Medium | [1373_workflow_1373.json](workflows/1373_workflow_1373.json) |
| 1374_workflow_1374 | automate | notion, webhook | 🔴 High | [1374_workflow_1374.json](workflows/1374_workflow_1374.json) |
| 1394_workflow_1394 | automate | awstranscribe, googlesheets, awss3 | 🟡 Medium | [1394_workflow_1394.json](workflows/1394_workflow_1394.json) |
| 1395_workflow_1395 | automate | httprequest, awsrekognition, googlesheets | 🟡 Medium | [1395_workflow_1395.json](workflows/1395_workflow_1395.json) |
| 1401_workflow_1401 | automate | googlesheets, httprequest, awsrekognition | 🟢 Low | [1401_workflow_1401.json](workflows/1401_workflow_1401.json) |
| 1455_workflow_1455 | automate | crypto, httprequest, webhook | 🔴 High | [1455_workflow_1455.json](workflows/1455_workflow_1455.json) |
| 1489_workflow_1489 | automate | httprequest, webhook, googlesheets | 🟡 Medium | [1489_workflow_1489.json](workflows/1489_workflow_1489.json) |
| 1520_workflow_1520 | automate | httprequest, functionitem, manual | 🟢 Low | [1520_workflow_1520.json](workflows/1520_workflow_1520.json) |
| 1736_workflow_1736 | automate | googlesheets, movebinarydata, readbinaryfile | 🟢 Low | [1736_workflow_1736.json](workflows/1736_workflow_1736.json) |
| 1737_workflow_1737 | automate | spreadsheetfile, httprequest, googlesheets | 🟡 Medium | [1737_workflow_1737.json](workflows/1737_workflow_1737.json) |
| 1751_workflow_1751 | automate | n8ntrainingcustomerdatastore, manual, googlesheets | 🟡 Medium | [1751_workflow_1751.json](workflows/1751_workflow_1751.json) |
| 1752_workflow_1752 | automate | googlesheets, mysql, cron | 🟢 Low | [1752_workflow_1752.json](workflows/1752_workflow_1752.json) |
| 1753_workflow_1753 | automate | googlesheets, mysql, cron | 🟢 Low | [1753_workflow_1753.json](workflows/1753_workflow_1753.json) |
| 1754_workflow_1754 | automate | interval, manual, googlesheets | 🟡 Medium | [1754_workflow_1754.json](workflows/1754_workflow_1754.json) |
| 1756_workflow_1756 | automate | spreadsheetfile, googlesheets, webhook | 🟢 Low | [1756_workflow_1756.json](workflows/1756_workflow_1756.json) |
| 1757_workflow_1757 | automate | googlesheets, webhook, respondtowebhook | 🟢 Low | [1757_workflow_1757.json](workflows/1757_workflow_1757.json) |
| 1769_workflow_1769 | automate | asana, notion, asana | 🟡 Medium | [1769_workflow_1769.json](workflows/1769_workflow_1769.json) |
| 1791_workflow_1791 | automate | googlesheets, movebinarydata, readbinaryfile | 🟢 Low | [1791_workflow_1791.json](workflows/1791_workflow_1791.json) |
| 1804_workflow_1804 | automate | github, notion | 🟡 Medium | [1804_workflow_1804.json](workflows/1804_workflow_1804.json) |
| 1810_workflow_1810 | automate | itemlists, httprequest, xml | 🟡 Medium | [1810_workflow_1810.json](workflows/1810_workflow_1810.json) |
| 1819_workflow_1819 | automate | notion, googledrive | 🟢 Low | [1819_workflow_1819.json](workflows/1819_workflow_1819.json) |
| 1834_workflow_1834 | automate | webhook, notion | 🟢 Low | [1834_workflow_1834.json](workflows/1834_workflow_1834.json) |
| 1835_workflow_1835 | automate | notion, clickup, clickup | 🟢 Low | [1835_workflow_1835.json](workflows/1835_workflow_1835.json) |
| 1839_workflow_1839 | automate | spreadsheetfile, mysql, manual | 🟢 Low | [1839_workflow_1839.json](workflows/1839_workflow_1839.json) |
| 1872_workflow_1872 | automate | spreadsheetfile, manual, mysql | 🟢 Low | [1872_workflow_1872.json](workflows/1872_workflow_1872.json) |
| 1930_workflow_1930 | automate | manual, googlesheets, postgres | 🟡 Medium | [1930_workflow_1930.json](workflows/1930_workflow_1930.json) |
| 1933_workflow_1933 | automate | spreadsheetfile, httprequest, manual | 🟡 Medium | [1933_workflow_1933.json](workflows/1933_workflow_1933.json) |
| 1945_workflow_1945 | automate | itemlists, datetime, httprequest | 🟡 Medium | [1945_workflow_1945.json](workflows/1945_workflow_1945.json) |
| 1949_workflow_1949 | automate | itemlists, xml, manual | 🔴 High | [1949_workflow_1949.json](workflows/1949_workflow_1949.json) |
| 1_workflow_1 | automate | spreadsheetfile, postgres, readbinaryfile | 🟢 Low | [1_workflow_1.json](workflows/1_workflow_1.json) |
| 2014_workflow_2014 | automate | httprequest, manual, googlesheets | 🟡 Medium | [2014_workflow_2014.json](workflows/2014_workflow_2014.json) |
| 2015_workflow_2015 | automate | httprequest, manual, googlesheets | 🟡 Medium | [2015_workflow_2015.json](workflows/2015_workflow_2015.json) |
| 2016_workflow_2016 | automate | httprequest, manual, googlesheets | 🟡 Medium | [2016_workflow_2016.json](workflows/2016_workflow_2016.json) |
| 2034_workflow_2034 | automate | httprequest, webhook, mysql | 🟢 Low | [2034_workflow_2034.json](workflows/2034_workflow_2034.json) |
| 2037_workflow_2037 | automate | manual, airtable | 🟢 Low | [2037_workflow_2037.json](workflows/2037_workflow_2037.json) |
| 2038_workflow_2038 | automate | webhook, notion | 🟢 Low | [2038_workflow_2038.json](workflows/2038_workflow_2038.json) |
| 2063_workflow_2063 | automate | itemlists, httprequest, schedule | 🔴 High | [2063_workflow_2063.json](workflows/2063_workflow_2063.json) |
| 2071_workflow_2071 | automate | spreadsheetfile, httprequest, airtable | 🔴 High | [2071_workflow_2071.json](workflows/2071_workflow_2071.json) |
| 2076_workflow_2076 | automate | itemlists, httprequest, schedule | 🔴 High | [2076_workflow_2076.json](workflows/2076_workflow_2076.json) |
| 2107_workflow_2107 | automate | httprequest, schedule, googlesheets | 🟡 Medium | [2107_workflow_2107.json](workflows/2107_workflow_2107.json) |
| 2113_workflow_2113 | automate | httprequest, schedule, googlesheets | 🔴 High | [2113_workflow_2113.json](workflows/2113_workflow_2113.json) |
| 2140_workflow_2140 | automate | httprequest, notion, webhook | 🟡 Medium | [2140_workflow_2140.json](workflows/2140_workflow_2140.json) |
| 2141_workflow_2141 | automate | httprequest, webhook, googlesheets | 🟡 Medium | [2141_workflow_2141.json](workflows/2141_workflow_2141.json) |
| 2148_workflow_2148 | automate | graphql, schedule, googlesheets | 🔴 High | [2148_workflow_2148.json](workflows/2148_workflow_2148.json) |
| 2151_workflow_2151 | automate | httprequest, notion, schedule | 🟡 Medium | [2151_workflow_2151.json](workflows/2151_workflow_2151.json) |
| 2169_workflow_2169 | automate | postgres, schedule, manual | 🟡 Medium | [2169_workflow_2169.json](workflows/2169_workflow_2169.json) |
| 2191_workflow_2191 | automate | httprequest, googlesheets, removeduplicates | 🟡 Medium | [2191_workflow_2191.json](workflows/2191_workflow_2191.json) |
| 2199_workflow_2199 | automate | schedule, googlesheets, twitter | 🟢 Low | [2199_workflow_2199.json](workflows/2199_workflow_2199.json) |
| 2267_workflow_2267 | automate | httprequest, manual, airtable | 🟡 Medium | [2267_workflow_2267.json](workflows/2267_workflow_2267.json) |
| 226_workflow_226 | automate | googlesheets, webhook | 🟢 Low | [226_workflow_226.json](workflows/226_workflow_226.json) |
| 2281_workflow_2281 | automate | wordpress, httprequest, markdown | 🔴 High | [2281_workflow_2281.json](workflows/2281_workflow_2281.json) |
| 2409_workflow_2409 | automate | emailsend, pushover, notion | 🔴 High | [2409_workflow_2409.json](workflows/2409_workflow_2409.json) |
| 2550_workflow_2550 | automate | crypto, emailsend, form | 🔴 High | [2550_workflow_2550.json](workflows/2550_workflow_2550.json) |
| 2555_workflow_2555 | automate | googlesheets, webflow | 🟡 Medium | [2555_workflow_2555.json](workflows/2555_workflow_2555.json) |
| 2566_workflow_2566 | automate | n8n-nodes-langchain.memorybufferwindow, respondtowebhook, crypto | 🔴 High | [2566_workflow_2566.json](workflows/2566_workflow_2566.json) |
| 2603_workflow_2603 | automate | httprequest, form, airtable | 🔴 High | [2603_workflow_2603.json](workflows/2603_workflow_2603.json) |
| 2613_workflow_2613 | automate | httprequest, schedule, googlesheets | 🔴 High | [2613_workflow_2613.json](workflows/2613_workflow_2613.json) |
| 2661_workflow_2661 | automate | httprequest, webhook, airtable | 🔴 High | [2661_workflow_2661.json](workflows/2661_workflow_2661.json) |
| 2678_workflow_2678 | automate | strava, schedule, sort | 🔴 High | [2678_workflow_2678.json](workflows/2678_workflow_2678.json) |
| 2796_workflow_2796 | automate | httprequest, webhook, googlecalendar | 🔴 High | [2796_workflow_2796.json](workflows/2796_workflow_2796.json) |
| 2802_workflow_2802 | automate | splitinbatches, httprequest, notion | 🔴 High | [2802_workflow_2802.json](workflows/2802_workflow_2802.json) |
| 2808_workflow_2808 | automate | httprequest, manual, googlesheets | 🟡 Medium | [2808_workflow_2808.json](workflows/2808_workflow_2808.json) |
| 2901_workflow_2901 | automate | httprequest, notion, notion | 🟡 Medium | [2901_workflow_2901.json](workflows/2901_workflow_2901.json) |
| 2_workflow_2 | automate | postgres, writebinaryfile, spreadsheetfile | 🟢 Low | [2_workflow_2.json](workflows/2_workflow_2.json) |
| 3032_workflow_3032 | automate | splitinbatches, gong, comparedatasets | 🔴 High | [3032_workflow_3032.json](workflows/3032_workflow_3032.json) |
| 3036_workflow_3036 | automate | httprequest, notion, executeworkflow | 🔴 High | [3036_workflow_3036.json](workflows/3036_workflow_3036.json) |
| 3037_workflow_3037 | automate | notion, executeworkflow | 🔴 High | [3037_workflow_3037.json](workflows/3037_workflow_3037.json) |
| 3039_workflow_3039 | automate | notion, executeworkflow | 🔴 High | [3039_workflow_3039.json](workflows/3039_workflow_3039.json) |
| 3218_workflow_3218 | automate | httprequest, schedule, manual | 🟡 Medium | [3218_workflow_3218.json](workflows/3218_workflow_3218.json) |
| 3233_workflow_3233 | automate | httprequest, schedule, manual | 🟡 Medium | [3233_workflow_3233.json](workflows/3233_workflow_3233.json) |
| 3280_workflow_3280 | automate | httprequest, schedule, manual | 🔴 High | [3280_workflow_3280.json](workflows/3280_workflow_3280.json) |
| 3332_workflow_3332 | automate | googlesheets, googledrive | 🟢 Low | [3332_workflow_3332.json](workflows/3332_workflow_3332.json) |
| 3385_workflow_3385 | automate | googlesheets, webhook, respondtowebhook | 🟡 Medium | [3385_workflow_3385.json](workflows/3385_workflow_3385.json) |
| 3427_workflow_3427 | automate | itemlists, webhook, googlecalendar | 🔴 High | [3427_workflow_3427.json](workflows/3427_workflow_3427.json) |
| 3463_workflow_3463 | automate | splitinbatches, rssfeedread, markdown | 🔴 High | [3463_workflow_3463.json](workflows/3463_workflow_3463.json) |
| 3476_workflow_3476 | automate | googlesheets, manual, airtop | 🟢 Low | [3476_workflow_3476.json](workflows/3476_workflow_3476.json) |
| 3504_workflow_3504 | automate | notion, webhook, airtable | 🔴 High | [3504_workflow_3504.json](workflows/3504_workflow_3504.json) |
| 3556_workflow_3556 | automate | httprequest, schedule, googlesheets | 🟡 Medium | [3556_workflow_3556.json](workflows/3556_workflow_3556.json) |
| 3580_workflow_3580 | automate | httprequest, googlesheets, form | 🔴 High | [3580_workflow_3580.json](workflows/3580_workflow_3580.json) |
| 3588_workflow_3588 | automate | httprequest, schedule, googlesheets | 🟡 Medium | [3588_workflow_3588.json](workflows/3588_workflow_3588.json) |
| 3631_workflow_3631 | automate | postgres, postgres, n8n-nodes-langchain.mcp | 🔴 High | [3631_workflow_3631.json](workflows/3631_workflow_3631.json) |
| 3638_workflow_3638 | automate | httprequest, n8n-nodes-langchain.mcp, n8n-nodes-langchain.workflow | 🔴 High | [3638_workflow_3638.json](workflows/3638_workflow_3638.json) |
| 3785_workflow_3785 | automate | httprequest, form, manual | 🔴 High | [3785_workflow_3785.json](workflows/3785_workflow_3785.json) |
| 3849_workflow_3849 | automate | n8n-nodes-langchain.chainllm, reddit, n8n-nodes-langchain.chainsummarization | 🔴 High | [3849_workflow_3849.json](workflows/3849_workflow_3849.json) |
| 3901_workflow_3901 | automate | splitinbatches, n8n-nodes-langchain.chainllm, n8n-nodes-langchain.outputparserstructured | 🔴 High | [3901_workflow_3901.json](workflows/3901_workflow_3901.json) |
| 458_workflow_458 | automate | postgres, manual | 🟢 Low | [458_workflow_458.json](workflows/458_workflow_458.json) |
| 503_workflow_503 | automate | mongodb, manual | 🟢 Low | [503_workflow_503.json](workflows/503_workflow_503.json) |
| 598_workflow_598 | automate | manual, mysql | 🟢 Low | [598_workflow_598.json](workflows/598_workflow_598.json) |
| 599_workflow_599 | automate | postgres, manual | 🟢 Low | [599_workflow_599.json](workflows/599_workflow_599.json) |
| 600_workflow_600 | automate | googlesheets, manual | 🟢 Low | [600_workflow_600.json](workflows/600_workflow_600.json) |
| 636_workflow_636 | automate | mautic, googlesheets, cron | 🟢 Low | [636_workflow_636.json](workflows/636_workflow_636.json) |
| 6_workflow_6 | automate | googlesheets, cron | 🟢 Low | [6_workflow_6.json](workflows/6_workflow_6.json) |
| 738_workflow_738 | automate | openweathermap, webhook, airtable | 🟢 Low | [738_workflow_738.json](workflows/738_workflow_738.json) |
| 739_workflow_739 | automate | airtable, webhook, mindee | 🟢 Low | [739_workflow_739.json](workflows/739_workflow_739.json) |
| 933_workflow_933 | automate | getresponse, airtable | 🟢 Low | [933_workflow_933.json](workflows/933_workflow_933.json) |
| 983_workflow_983 | automate | lemlist, airtable | 🟢 Low | [983_workflow_983.json](workflows/983_workflow_983.json) |
| 991_workflow_991 | automate | autopilot, airtable | 🟢 Low | [991_workflow_991.json](workflows/991_workflow_991.json) |
| 993_workflow_993 | automate | wise, wise, airtable | 🟢 Low | [993_workflow_993.json](workflows/993_workflow_993.json) |
| AccountCraft WhatsApp Automation - Infridet | automate | googlesheets, emailsend, webhook | 🟢 Low | [3808_AccountCraft_WhatsApp_Automation_-_Infridet.json](workflows/3808_AccountCraft_WhatsApp_Automation_-_Infridet.json) |
| Amazon keywords | automate | httprequest, webhook, airtable | 🟡 Medium | [kJMoiGRorIlsTYZv_Amazon_keywords.json](workflows/kJMoiGRorIlsTYZv_Amazon_keywords.json) |
| AutoQoutesV2_template | automate | httprequest, executecommand, readwritefile | 🔴 High | [CvXjXG4SFnN0ioJQ_AutoQoutesV2_template.json](workflows/CvXjXG4SFnN0ioJQ_AutoQoutesV2_template.json) |
| Automate Event Creation in Google Calendar from Google Sheets | automate | googlecalendar, googlesheets | 🟢 Low | [AvCMhDoSUAYXsrQX_Automate_Event_Creation_in_Google_Calendar_from_Google_Sheets.json](workflows/AvCMhDoSUAYXsrQX_Automate_Event_Creation_in_Google_Calendar_from_Google_Sheets.json) |
| Automated Work Attendance with Location Triggers | automate | webhook, googledrive, googlesheets | 🟡 Medium | [x2kgOnBLtqAjqUVS_Automated_Work_Attendance_with_Location_Triggers.json](workflows/x2kgOnBLtqAjqUVS_Automated_Work_Attendance_with_Location_Triggers.json) |
| Bubble Data Access | automate | httprequest, manual | 🟢 Low | [15_Bubble_Data_Access.json](workflows/15_Bubble_Data_Access.json) |
| CFP Selection 1 | automate | typeform, airtable | 🟢 Low | [54_CFP_Selection_1.json](workflows/54_CFP_Selection_1.json) |
| CFP Selection 2 | automate | trello, bannerbear, manual | 🟢 Low | [55_CFP_Selection_2.json](workflows/55_CFP_Selection_2.json) |
| Capture Website Screenshots with Bright Data Web Unlocker and Save to Disk | automate | httprequest, readwritefile, manual | 🟡 Medium | [1U5Jf4NMQEw9LtxY_Capture_Website_Screenshots_with_Bright_Data_Web_Unlocker_and_Save_to_Disk.json](workflows/1U5Jf4NMQEw9LtxY_Capture_Website_Screenshots_with_Bright_Data_Web_Unlocker_and_Save_to_Disk.json) |
| Compare 2 SQL datasets | automate | comparedatasets, manual, mysql | 🟢 Low | [emPRhyWgxygwHgWh_Compare_2_SQL_datasets.json](workflows/emPRhyWgxygwHgWh_Compare_2_SQL_datasets.json) |
| Congratulations Workflow | automate | cron, googlesheets, twilio | 🟡 Medium | [247_Congratulations_Workflow.json](workflows/247_Congratulations_Workflow.json) |
| Exponential Backoff for Google APIs | automate | splitinbatches, stopanderror, manual | 🟡 Medium | [2NhqmUqW3KruEkaE_Exponential_Backoff_for_Google_APIs.json](workflows/2NhqmUqW3KruEkaE_Exponential_Backoff_for_Google_APIs.json) |
| Form with Dynamic Dropdown Field | automate | googlesheets, n8n, executeworkflow | 🔴 High | [RKbQHfblpcvMGZ4w_Form_with_Dynamic_Dropdown_Field.json](workflows/RKbQHfblpcvMGZ4w_Form_with_Dynamic_Dropdown_Field.json) |
| GoogleSheets MySQL Integration | automate | comparedatasets, schedule, manual | 🔴 High | [VtiRiIGkdeUhyh0N_GoogleSheets_MySQL_Integration.json](workflows/VtiRiIGkdeUhyh0N_GoogleSheets_MySQL_Integration.json) |
| ICP Company Scoring | automate | googlesheets, manual, airtop | 🟢 Low | [xyLfWaqdIoZmbTfv_ICP_Company_Scoring.json](workflows/xyLfWaqdIoZmbTfv_ICP_Company_Scoring.json) |
| Image-to-3D | automate | httprequest, schedule, manual | 🔴 High | [XiwLd0JwGmDoY0mr_Image-to-3D.json](workflows/XiwLd0JwGmDoY0mr_Image-to-3D.json) |
| LINE BOT - Google Sheets Record Receipt | automate | httprequest, webhook, googledrive | 🟡 Medium | [QOePbDNCilLhfzbs_LINE_BOT_-_Google_Sheets_Record_Receipt.json](workflows/QOePbDNCilLhfzbs_LINE_BOT_-_Google_Sheets_Record_Receipt.json) |
| Line Save File to Google Drive and Log File's URL | automate | httprequest, webhook, googledrive | 🔴 High | [mqdP7Aw1KnkIq2W5_Line_Save_File_to_Google_Drive_and_Log_File's_URL.json](workflows/mqdP7Aw1KnkIq2W5_Line_Save_File_to_Google_Drive_and_Log_File's_URL.json) |
| LinkedIn Profile Discovery | automate | googlesheets, manual, airtop | 🟢 Low | [lifB7iUXlDzr5dmI_LinkedIn_Profile_Discovery.json](workflows/lifB7iUXlDzr5dmI_LinkedIn_Profile_Discovery.json) |
| Linkedin Chrome Extensions | automate | splitinbatches, httprequest, manual | 🟡 Medium | [H9uAqvTaO7nTFdsH_Linkedin_Chrome_Extensions.json](workflows/H9uAqvTaO7nTFdsH_Linkedin_Chrome_Extensions.json) |
| List Builder | automate | airtop, manual, googlesheets | 🟡 Medium | [VwU1zMhcgzgPS9ak_List_Builder.json](workflows/VwU1zMhcgzgPS9ak_List_Builder.json) |
| Moving metrics from Google Sheets to Orbit | automate | googlesheets, orbit | 🟢 Low | [829_Moving_metrics_from_Google_Sheets_to_Orbit.json](workflows/829_Moving_metrics_from_Google_Sheets_to_Orbit.json) |
| My workflow 2 | automate | splitinbatches, httprequest, schedule | 🔴 High | [Eyh4jc7RK7rCTh4z_My_workflow_2.json](workflows/Eyh4jc7RK7rCTh4z_My_workflow_2.json) |
| New tweets | automate | manual, airtable, twitter | 🟡 Medium | [1003_New_tweets.json](workflows/1003_New_tweets.json) |
| Notion to Linkedin | automate | httprequest, linkedin, notion | 🔴 High | [0pVPSW4PzJZLLqSf_Notion_to_Linkedin.json](workflows/0pVPSW4PzJZLLqSf_Notion_to_Linkedin.json) |
| OCR receipts from Google Drive | automate | httprequest, manual, googledrive | 🟡 Medium | [dVDyWWhO5FdPM3qx_OCR_receipts_from_Google_Drive.json](workflows/dVDyWWhO5FdPM3qx_OCR_receipts_from_Google_Drive.json) |
| Postgres Data Ingestion | automate | postgres, cron | 🟢 Low | [33_Postgres_Data_Ingestion.json](workflows/33_Postgres_Data_Ingestion.json) |
| ProspectLens company research | automate | splitinbatches, httprequest, manual | 🟡 Medium | [wwvUsosYUyMfpGbB_ProspectLens_company_research.json](workflows/wwvUsosYUyMfpGbB_ProspectLens_company_research.json) |
| Smart Factory Data Generator | automate | amqp, interval | 🟢 Low | [167_Smart_Factory_Data_Generator.json](workflows/167_Smart_Factory_Data_Generator.json) |
| TEMPLATE - Multi Methods API Endpoint | automate | webhook, airtable, respondtowebhook | 🔴 High | [GWXjIqENWvx6OqvX_TEMPLATE_-_Multi_Methods_API_Endpoint.json](workflows/GWXjIqENWvx6OqvX_TEMPLATE_-_Multi_Methods_API_Endpoint.json) |
| Workflow management | automate | splitinbatches, movebinarydata, dropbox | 🔴 High | [48_Workflow_management.json](workflows/48_Workflow_management.json) |
| Youtube Searcher | automate | splitinbatches, postgres, httprequest | 🔴 High | [Zrd98BnbmN1Px9an_Youtube_Searcher.json](workflows/Zrd98BnbmN1Px9an_Youtube_Searcher.json) |
| [1/3 - anomaly detection] [1/2 - KNN classification] Batch upload dataset to Qdrant (crops dataset) | automate | httprequest, googlecloudstorage, manual | 🔴 High | [pPtCy6qPfEv1qNRn_[1_3_-_anomaly_detection]_[1_2_-_KNN_classification]_Batch_upload_dataset_to_Qdrant_(crops_dataset).json](workflows/pPtCy6qPfEv1qNRn_[1_3_-_anomaly_detection]_[1_2_-_KNN_classification]_Batch_upload_dataset_to_Qdrant_(crops_dataset).json) |
| [1/3 - anomaly detection] [1/2 - KNN classification] Batch upload dataset to Qdrant (crops dataset) | automate | httprequest, googlecloudstorage, manual | 🔴 High | [Vector Database as a Big Data Analysis Tool for AI Agents [1_3 anomaly][1_2 KNN].json](workflows/Vector Database as a Big Data Analysis Tool for AI Agents [1_3 anomaly][1_2 KNN].json) |
| [2/2] KNN classifier (lands dataset) | automate | httprequest, executeworkflow | 🔴 High | [Vector Database as a Big Data Analysis Tool for AI Agents [2_2 KNN].json](workflows/Vector Database as a Big Data Analysis Tool for AI Agents [2_2 KNN].json) |
| [2/2] KNN classifier (lands dataset) | automate | httprequest, executeworkflow | 🔴 High | [Vector Database as a Big Data Analysis Tool for AI Agents [2_2 KNN] (1).json](workflows/Vector Database as a Big Data Analysis Tool for AI Agents [2_2 KNN] (1).json) |
| [2/2] KNN classifier (lands dataset) | automate | httprequest, executeworkflow | 🔴 High | [itzURpN5wbUNOXOw_[2_2]_KNN_classifier_(lands_dataset).json](workflows/itzURpN5wbUNOXOw_[2_2]_KNN_classifier_(lands_dataset).json) |
| [2/3] Set up medoids (2 types) for anomaly detection (crops dataset) | automate | httprequest, manual | 🔴 High | [m9aACcHqydEbH4nR_[2_3]_Set_up_medoids_(2_types)_for_anomaly_detection_(crops_dataset).json](workflows/m9aACcHqydEbH4nR_[2_3]_Set_up_medoids_(2_types)_for_anomaly_detection_(crops_dataset).json) |
| [2/3] Set up medoids (2 types) for anomaly detection (crops dataset) | automate | httprequest, manual | 🔴 High | [Vector Database as a Big Data Analysis Tool for AI Agents [2_3 - anomaly].json](workflows/Vector Database as a Big Data Analysis Tool for AI Agents [2_3 - anomaly].json) |
| [3/3] Anomaly detection tool (crops dataset) | automate | httprequest, executeworkflow | 🔴 High | [Automated Hugging Face Paper Summary Fetching & Categorization Workflow.json](workflows/Automated Hugging Face Paper Summary Fetching & Categorization Workflow.json) |
| [3/3] Anomaly detection tool (crops dataset) | automate | httprequest, executeworkflow | 🔴 High | [G8jRDBvwsMkkMiLN_[3_3]_Anomaly_detection_tool_(crops_dataset).json](workflows/G8jRDBvwsMkkMiLN_[3_3]_Anomaly_detection_tool_(crops_dataset).json) |
| [3/3] Anomaly detection tool (crops dataset) | automate | httprequest, executeworkflow | 🔴 High | [Vector Database as a Big Data Analysis Tool for AI Agents [3_3 - anomaly].json](workflows/Vector Database as a Big Data Analysis Tool for AI Agents [3_3 - anomaly].json) |
| n8n-農產品 | automate | googlesheets, httprequest, manual | 🟢 Low | [ziJG3tgG91Gkbina_n8n-農產品.json](workflows/ziJG3tgG91Gkbina_n8n-農產品.json) |
| n8n_mysql_purge_history_greater_than_10_days | automate | cron, manual, mysql | 🟢 Low | [60_n8n_mysql_purge_history_greater_than_10_days.json](workflows/60_n8n_mysql_purge_history_greater_than_10_days.json) |
| typeform feedback workflow | automate | googlesheets, typeform | 🟢 Low | [1001_typeform_feedback_workflow.json](workflows/1001_typeform_feedback_workflow.json) |
| 💥workflow n8n d'Auto-Post sur les réseaux sociaux - vide | automate | httprequest, schedule, googlesheets | 🟡 Medium | [CCcz1G4G2yPwk1me_💥workflow_n8n_d'Auto-Post_sur_les_réseaux_sociaux_-_vide.json](workflows/CCcz1G4G2yPwk1me_💥workflow_n8n_d'Auto-Post_sur_les_réseaux_sociaux_-_vide.json) |
| Archive empty pages in Notion Database | backup | splitinbatches, notion, cron | 🟡 Medium | [115_Archive_empty_pages_in_Notion_Database.json](workflows/115_Archive_empty_pages_in_Notion_Database.json) |
| 🧹 Archive (delete) duplicate items from a Notion database | backup | notion, schedule, notion | 🟡 Medium | [As8TxF3PjyXygc0o_🧹_Archive_(delete)_duplicate_items_from_a_Notion_database.json](workflows/As8TxF3PjyXygc0o_🧹_Archive_(delete)_duplicate_items_from_a_Notion_database.json) |
| Add a datapoint to Beeminder when new activity is added to Strava | create | beeminder, strava | 🟢 Low | [208_Add_a_datapoint_to_Beeminder_when_new_activity_is_added_to_Strava.json](workflows/208_Add_a_datapoint_to_Beeminder_when_new_activity_is_added_to_Strava.json) |
| Add new clients from Notion to Clockify | create | notion, clockify | 🟢 Low | [mbgpq1PH1SFkHi6w_Add_new_clients_from_Notion_to_Clockify.json](workflows/mbgpq1PH1SFkHi6w_Add_new_clients_from_Notion_to_Clockify.json) |
| Create a table and insert data into it | create | questdb, manual | 🟢 Low | [161_Create_a_table_and_insert_data_into_it.json](workflows/161_Create_a_table_and_insert_data_into_it.json) |
| Create a table, and insert and update data in the table in Snowflake | create | snowflake, manual | 🟢 Low | [172_Create_a_table,_and_insert_and_update_data_in_the_table_in_Snowflake.json](workflows/172_Create_a_table,_and_insert_and_update_data_in_the_table_in_Snowflake.json) |
| Insert data into a new row for a table in Coda | create | manual, coda | 🟢 Low | [102_Insert_data_into_a_new_row_for_a_table_in_Coda.json](workflows/102_Insert_data_into_a_new_row_for_a_table_in_Coda.json) |
| Create Onfleet tasks from Spreadsheets | create_task | spreadsheetfile, onfleet, readbinaryfile | 🟢 Low | [12_Create_Onfleet_tasks_from_Spreadsheets.json](workflows/12_Create_Onfleet_tasks_from_Spreadsheets.json) |
| Fetch Squarespace Blog & Event Collections to Google Sheets   | extract | httprequest, schedule, manual | 🟡 Medium | [sUGieRWulZJ7scll_Fetch_Squarespace_Blog_&_Event_Collections_to_Google_Sheets__.json](workflows/sUGieRWulZJ7scll_Fetch_Squarespace_Blog_&_Event_Collections_to_Google_Sheets__.json) |
| Scrape Trustpilot Reviews to Google Sheets | extract | httprequest, schedule, manual | 🔴 High | [DqvkhR9nzoPQKxGh_Scrape_Trustpilot_Reviews_to_Google_Sheets.json](workflows/DqvkhR9nzoPQKxGh_Scrape_Trustpilot_Reviews_to_Google_Sheets.json) |
| Structured Bulk Data Extract with Bright Data Web Scraper | extract | httprequest, readwritefile, manual | 🔴 High | [OjwmaLrXhW4pO5ph_Structured_Bulk_Data_Extract_with_Bright_Data_Web_Scraper.json](workflows/OjwmaLrXhW4pO5ph_Structured_Bulk_Data_Extract_with_Bright_Data_Web_Scraper.json) |
| extract_swifts | extract | splitinbatches, htmlextract, uproc | 🔴 High | [14_extract_swifts.json](workflows/14_extract_swifts.json) |
| AutoClip – Automatically Generate Video Clips and Upload to YouTube | generate | httprequest, executecommand, readwritefile | 🔴 High | [gI3QGKTf52zwyh6O_AutoClip_–_Automatically_Generate_Video_Clips_and_Upload_to_YouTube.json](workflows/gI3QGKTf52zwyh6O_AutoClip_–_Automatically_Generate_Video_Clips_and_Upload_to_YouTube.json) |
| Generate New Keywords with Search Volumes⚒️⚒️🟢🟢 | generate | httprequest, googlesheets, executeworkflow | 🟡 Medium | [SiQUWOBCyXCAA5f9_Generate_New_Keywords_with_Search_Volumes⚒️⚒️🟢🟢.json](workflows/SiQUWOBCyXCAA5f9_Generate_New_Keywords_with_Search_Volumes⚒️⚒️🟢🟢.json) |
| Amazon Product Price Tracker | monitor | splitinbatches, emailsend, httprequest | 🔴 High | [TqnC0nyAa0LRfYBX_Amazon_Product_Price_Tracker.json](workflows/TqnC0nyAa0LRfYBX_Amazon_Product_Price_Tracker.json) |
| Expense Tracker App | monitor | httprequest, mindee, airtable | 🟢 Low | [55_Expense_Tracker_App.json](workflows/55_Expense_Tracker_App.json) |
| Track Working Time and Pauses | monitor | notion, webhook, respondtowebhook | 🔴 High | [pdgNdag49lwoTxUP_Track_Working_Time_and_Pauses.json](workflows/pdgNdag49lwoTxUP_Track_Working_Time_and_Pauses.json) |
| Convert image from jpg/png to webp | process | httprequest, manual, googledrive | 🟡 Medium | [IyDJ7Zgh4MV43YTh_Convert_image_from_jpg_png_to_webp.json](workflows/IyDJ7Zgh4MV43YTh_Convert_image_from_jpg_png_to_webp.json) |
| Get Product Feedback | read | trello, airtable, typeform | 🟡 Medium | [65_Get_Product_Feedback.json](workflows/65_Get_Product_Feedback.json) |
| Get all orders in Squarespace to Google Sheets | read | httprequest, schedule, manual | 🟡 Medium | [cRprVEUCjjvozkfb_Get_all_orders_in_Squarespace_to_Google_Sheets.json](workflows/cRprVEUCjjvozkfb_Get_all_orders_in_Squarespace_to_Google_Sheets.json) |
| Get the current weather data for a city | read | openweathermap, manual | 🟢 Low | [88_Get_the_current_weather_data_for_a_city.json](workflows/88_Get_the_current_weather_data_for_a_city.json) |
| Loading data into a spreadsheet | read | manual | 🟢 Low | [1028_Loading_data_into_a_spreadsheet.json](workflows/1028_Loading_data_into_a_spreadsheet.json) |
| Clockify to Syncro | sync | httprequest, webhook, googlesheets | 🟡 Medium | [3_Clockify_to_Syncro.json](workflows/3_Clockify_to_Syncro.json) |
| Dialpad to Syncro | sync | httprequest, webhook, googlesheets | 🔴 High | [1_Dialpad_to_Syncro.json](workflows/1_Dialpad_to_Syncro.json) |
| Entra Contacts to Zammad User Sync | sync | httprequest, comparedatasets, manual | 🔴 High | [ikxQzs58WxtUjbuE_Entra_Contacts_to_Zammad_User_Sync.json](workflows/ikxQzs58WxtUjbuE_Entra_Contacts_to_Zammad_User_Sync.json) |
| Entra User to Zammad User Sync | sync | httprequest, comparedatasets, manual | 🔴 High | [KKCfXEpBjjhp1LC8_Entra_User_to_Zammad_User_Sync.json](workflows/KKCfXEpBjjhp1LC8_Entra_User_to_Zammad_User_Sync.json) |
| Notion to Clockify Sync Template | sync | httprequest, comparedatasets, stopanderror | 🔴 High | [HpjjgJm3Ulnl1cJQ_Notion_to_Clockify_Sync_Template.json](workflows/HpjjgJm3Ulnl1cJQ_Notion_to_Clockify_Sync_Template.json) |
| Shopify to Google Sheets Product Sync Automation | sync | graphql, schedule, googlesheets | 🔴 High | [WBkJdubQjVzMUhwi_Shopify_to_Google_Sheets_Product_Sync_Automation.json](workflows/WBkJdubQjVzMUhwi_Shopify_to_Google_Sheets_Product_Sync_Automation.json) |
| Spotify Sync Liked Songs to Playlist | sync | splitinbatches, gotify, comparedatasets | 🔴 High | [gemC8tYGZk3LtBHG_Spotify_Sync_Liked_Songs_to_Playlist.json](workflows/gemC8tYGZk3LtBHG_Spotify_Sync_Liked_Songs_to_Playlist.json) |
| Sync Jira issues with subsequent comments to Notion database | sync | jira, notion | 🟡 Medium | [YCQFaJdmJc6Rx4o7_Sync_Jira_issues_with_subsequent_comments_to_Notion_database.json](workflows/YCQFaJdmJc6Rx4o7_Sync_Jira_issues_with_subsequent_comments_to_Notion_database.json) |
| Sync New Shopify Products to Odoo Product | sync | odoo, shopify | 🟢 Low | [44PIIGwPzUe9dGfb_Sync_New_Shopify_Products_to_Odoo_Product.json](workflows/44PIIGwPzUe9dGfb_Sync_New_Shopify_Products_to_Odoo_Product.json) |
| Sync Todoist tasks to Notion | sync | schedule, todoist, notion | 🟢 Low | [PtPKIqDlz5xrrvHP_Sync_Todoist_tasks_to_Notion.json](workflows/PtPKIqDlz5xrrvHP_Sync_Todoist_tasks_to_Notion.json) |
| Sync Youtube Video Urls with Google Sheets | sync | httprequest, manual, googlesheets | 🟡 Medium | [rJNvM4vU6SLUeC1d_Sync_Youtube_Video_Urls_with_Google_Sheets.json](workflows/rJNvM4vU6SLUeC1d_Sync_Youtube_Video_Urls_with_Google_Sheets.json) |
| Synchronize your Google Sheets with Postgres | sync | postgres, comparedatasets, schedule | 🟡 Medium | [wDD4XugmHIvx3KMT_Synchronize_your_Google_Sheets_with_Postgres.json](workflows/wDD4XugmHIvx3KMT_Synchronize_your_Google_Sheets_with_Postgres.json) |
| Syncro Status Update Clockify | sync | webhook, httprequest, clockify | 🟢 Low | [5_Syncro_Status_Update_Clockify.json](workflows/5_Syncro_Status_Update_Clockify.json) |
| Syncro to Clockify | sync | webhook, clockify | 🟢 Low | [2_Syncro_to_Clockify.json](workflows/2_Syncro_to_Clockify.json) |
| How to automatically import CSV files into postgres | transfer | spreadsheetfile, postgres, manual | 🟢 Low | [q8GNbRhjQDwDpXoo_How_to_automatically_import_CSV_files_into_postgres.json](workflows/q8GNbRhjQDwDpXoo_How_to_automatically_import_CSV_files_into_postgres.json) |
| Import CSV from URL to GoogleSheet | transfer | spreadsheetfile, httprequest, manual | 🟡 Medium | [NLVfecejH0cTtcdd_Import_CSV_from_URL_to_GoogleSheet.json](workflows/NLVfecejH0cTtcdd_Import_CSV_from_URL_to_GoogleSheet.json) |
| Import multiple CSV to GoogleSheet | transfer | spreadsheetfile, splitinbatches, itemlists | 🟡 Medium | [zic2ZEHvxHR4UAYI_Import_multiple_CSV_to_GoogleSheet.json](workflows/zic2ZEHvxHR4UAYI_Import_multiple_CSV_to_GoogleSheet.json) |
| Import multiple Manufacturers from Google Sheets to Shopware 6 | transfer | splitinbatches, httprequest, manual | 🟡 Medium | [xLjE4IkQXARXOCZy_Import_multiple_Manufacturers_from_Google_Sheets_to_Shopware_6.json](workflows/xLjE4IkQXARXOCZy_Import_multiple_Manufacturers_from_Google_Sheets_to_Shopware_6.json) |
| PostgreSQL export to CSV | transfer | spreadsheetfile, manual, postgres | 🟢 Low | [39_PostgreSQL_export_to_CSV.json](workflows/39_PostgreSQL_export_to_CSV.json) |
| Append, lookup, update, and read data from a Google Sheets spreadsheet | update | googlesheets, manual | 🟢 Low | [5_Append,_lookup,_update,_and_read_data_from_a_Google_Sheets_spreadsheet.json](workflows/5_Append,_lookup,_update,_and_read_data_from_a_Google_Sheets_spreadsheet.json) |
| Receive updates for the position of the ISS every minute and push it to a database | update | googlefirebaserealtimedatabase, httprequest, cron | 🟢 Low | [134_Receive_updates_for_the_position_of_the_ISS_every_minute_and_push_it_to_a_database.json](workflows/134_Receive_updates_for_the_position_of_the_ISS_every_minute_and_push_it_to_a_database.json) |
| Update Crypto Values | update | coingecko, airtable, cron | 🟡 Medium | [14_Update_Crypto_Values.json](workflows/14_Update_Crypto_Values.json) |
| Live link checker | validate | splitinbatches, httprequest, manual | 🟡 Medium | [WGUpujme8ctIkBF8_Live_link_checker.json](workflows/WGUpujme8ctIkBF8_Live_link_checker.json) |
| Validate Seatable Webhooks with HMAC SHA256 Authentication | validate | crypto, webhook, respondtowebhook | 🟡 Medium | [W1ugowsjzt1SC4hH_Validate_Seatable_Webhooks_with_HMAC_SHA256_Authentication.json](workflows/W1ugowsjzt1SC4hH_Validate_Seatable_Webhooks_with_HMAC_SHA256_Authentication.json) |
| n8napi-check-workflow-which-model-is-using | validate | splitinbatches, n8n, manual | 🟡 Medium | [I2qMAcQET7isaqYD_n8napi-check-workflow-which-model-is-using.json](workflows/I2qMAcQET7isaqYD_n8napi-check-workflow-which-model-is-using.json) |

## BIZ

*60 workflows in this category*

| Workflow Name | Business Function | Key Integrations | Complexity | File |
|---------------|-------------------|------------------|------------|------|
|  | automate | paypal, manual | 🟢 Low | [438_.json](workflows/438_.json) |
| 1296_workflow_1296 | automate | hubspot, hubspot, clearbit | 🟢 Low | [1296_workflow_1296.json](workflows/1296_workflow_1296.json) |
| 1333_workflow_1333 | automate | pipedrive, hubspot, cron | 🟡 Medium | [1333_workflow_1333.json](workflows/1333_workflow_1333.json) |
| 1334_workflow_1334 | automate | pipedrive, hubspot, cron | 🟢 Low | [1334_workflow_1334.json](workflows/1334_workflow_1334.json) |
| 1758_workflow_1758 | automate | pipedrive, typeform | 🟡 Medium | [1758_workflow_1758.json](workflows/1758_workflow_1758.json) |
| 1775_workflow_1775 | automate | pipedrive, pipedrive, stripe | 🟡 Medium | [1775_workflow_1775.json](workflows/1775_workflow_1775.json) |
| 1776_workflow_1776 | automate | pipedrive, itemlists, stripe | 🟡 Medium | [1776_workflow_1776.json](workflows/1776_workflow_1776.json) |
| 1777_workflow_1777 | automate | pipedrive, itemlists, httprequest | 🟡 Medium | [1777_workflow_1777.json](workflows/1777_workflow_1777.json) |
| 1782_workflow_1782 | automate | pipedrive, pipedrive, itemlists | 🟡 Medium | [1782_workflow_1782.json](workflows/1782_workflow_1782.json) |
| 1787_workflow_1787 | automate | spreadsheetfile, pipedrive, googledrive | 🟡 Medium | [1787_workflow_1787.json](workflows/1787_workflow_1787.json) |
| 1788_workflow_1788 | automate | pipedrive, github, httprequest | 🟡 Medium | [1788_workflow_1788.json](workflows/1788_workflow_1788.json) |
| 1789_workflow_1789 | automate | pipedrive, github, httprequest | 🟡 Medium | [1789_workflow_1789.json](workflows/1789_workflow_1789.json) |
| 1792_workflow_1792 | automate | itemlists, renamekeys, manual | 🟡 Medium | [1792_workflow_1792.json](workflows/1792_workflow_1792.json) |
| 1793_workflow_1793 | automate | itemlists, renamekeys, manual | 🟡 Medium | [1793_workflow_1793.json](workflows/1793_workflow_1793.json) |
| 1794_workflow_1794 | automate | spreadsheetfile, itemlists, httprequest | 🔴 High | [1794_workflow_1794.json](workflows/1794_workflow_1794.json) |
| 1805_workflow_1805 | automate | hubspot, shopify | 🟡 Medium | [1805_workflow_1805.json](workflows/1805_workflow_1805.json) |
| 1806_workflow_1806 | automate | pipedrive, httprequest, functionitem | 🔴 High | [1806_workflow_1806.json](workflows/1806_workflow_1806.json) |
| 1807_workflow_1807 | automate | pipedrive, splitinbatches, itemlists | 🔴 High | [1807_workflow_1807.json](workflows/1807_workflow_1807.json) |
| 1840_workflow_1840 | automate | hubspot, functionitem, zendesk | 🟡 Medium | [1840_workflow_1840.json](workflows/1840_workflow_1840.json) |
| 1841_workflow_1841 | automate | hubspot, functionitem, zendesk | 🟡 Medium | [1841_workflow_1841.json](workflows/1841_workflow_1841.json) |
| 1855_workflow_1855 | automate | hubspot, itemlists, stripe | 🔴 High | [1855_workflow_1855.json](workflows/1855_workflow_1855.json) |
| 2111_workflow_2111 | automate | hubspot, httprequest, hubspot | 🟡 Medium | [2111_workflow_2111.json](workflows/2111_workflow_2111.json) |
| 2116_workflow_2116 | automate | hubspot, hunter, clearbit | 🟡 Medium | [2116_workflow_2116.json](workflows/2116_workflow_2116.json) |
| 2117_workflow_2117 | automate | hubspot, httprequest, schedule | 🔴 High | [2117_workflow_2117.json](workflows/2117_workflow_2117.json) |
| 2129_workflow_2129 | automate | hubspot, calendly, clearbit | 🔴 High | [2129_workflow_2129.json](workflows/2129_workflow_2129.json) |
| 2136_workflow_2136 | automate | pipedrive, hunter, clearbit | 🔴 High | [2136_workflow_2136.json](workflows/2136_workflow_2136.json) |
| 2610_workflow_2610 | automate | splitinbatches, postgres, hubspot | 🔴 High | [2610_workflow_2610.json](workflows/2610_workflow_2610.json) |
| 2807_workflow_2807 | automate | quickbooks, stripe, httprequest | 🟡 Medium | [2807_workflow_2807.json](workflows/2807_workflow_2807.json) |
| 3031_workflow_3031 | automate | gong, schedule, sort | 🟡 Medium | [3031_workflow_3031.json](workflows/3031_workflow_3031.json) |
| 3033_workflow_3033 | automate | httprequest, salesforce, executeworkflow | 🔴 High | [3033_workflow_3033.json](workflows/3033_workflow_3033.json) |
| 552_workflow_552 | automate | zohocrm, manual | 🟢 Low | [552_workflow_552.json](workflows/552_workflow_552.json) |
| 6 | automate | hubspot, manual | 🟢 Low | [7_6.json](workflows/7_6.json) |
| 628_workflow_628 | automate | hubspot | 🟢 Low | [628_workflow_628.json](workflows/628_workflow_628.json) |
| 664_workflow_664 | automate | manual, salesforce | 🟢 Low | [664_workflow_664.json](workflows/664_workflow_664.json) |
| Automate Drive-To-Store Lead Generation System (with coupon) on SuiteCRM | automate | respondtowebhook, httprequest, webhook | 🔴 High | [2890_Automate_Drive-To-Store_Lead_Generation_System_(with_coupon)_on_SuiteCRM.json](workflows/2890_Automate_Drive-To-Store_Lead_Generation_System_(with_coupon)_on_SuiteCRM.json) |
| INSEE Enrichment for Agile CRM | automate | httprequest, schedule, manual | 🔴 High | [G0hO05fypS8n8uYu_INSEE_Enrichment_for_Agile_CRM.json](workflows/G0hO05fypS8n8uYu_INSEE_Enrichment_for_Agile_CRM.json) |
| Lead Generation System (Template) | automate | httprequest, manual, airtable | 🟡 Medium | [EWIrJ8e9z7AijmTu_Lead_Generation_System_(Template).json](workflows/EWIrJ8e9z7AijmTu_Lead_Generation_System_(Template).json) |
| New WooCommerce Customer to Mautic | automate | mautic, woocommerce | 🟢 Low | [83_New_WooCommerce_Customer_to_Mautic.json](workflows/83_New_WooCommerce_Customer_to_Mautic.json) |
| Property Lead Contact Enrichment from CRM | automate | spreadsheetfile, hubspot, emailsend | 🔴 High | [RGVS0tHJV7Wh6aX4_Property_Lead_Contact_Enrichment_from_CRM.json](workflows/RGVS0tHJV7Wh6aX4_Property_Lead_Contact_Enrichment_from_CRM.json) |
| Send Typeforms leads via Whatsapp (Twilio) | automate | typeform, twilio | 🟢 Low | [1_Send_Typeforms_leads_via_Whatsapp_(Twilio).json](workflows/1_Send_Typeforms_leads_via_Whatsapp_(Twilio).json) |
| Unique QRcode coupon assignment and validation for Lead Generation system | automate | respondtowebhook, emailsend, httprequest | 🔴 High | [fW6PV9IaePKSMGbN_Unique_QRcode_coupon_assignment_and_validation_for_Lead_Generation_system.json](workflows/fW6PV9IaePKSMGbN_Unique_QRcode_coupon_assignment_and_validation_for_Lead_Generation_system.json) |
| [n8n] - Shopify Orders to D365 Business Central Sales Orders / Sales Invoices | automate | splitinbatches, shopify, httprequest | 🔴 High | [NGwD3pIHXBU0w5hC_[n8n]_-_Shopify_Orders_to_D365_Business_Central_Sales_Orders___Sales_Invoices.json](workflows/NGwD3pIHXBU0w5hC_[n8n]_-_Shopify_Orders_to_D365_Business_Central_Sales_Orders___Sales_Invoices.json) |
| Create Custom Presentations per Lead | create | googleslides, googledrive, extractfromfile | 🔴 High | [eF84e2NyJWTCVClW_Create_Custom_Presentations_per_Lead.json](workflows/eF84e2NyJWTCVClW_Create_Custom_Presentations_per_Lead.json) |
| Create a company in Salesmate | create | salesmate, manual | 🟢 Low | [128_Create_a_company_in_Salesmate.json](workflows/128_Create_a_company_in_Salesmate.json) |
| Create an deal in Pipedrive | create | pipedrive, manual | 🟢 Low | [113_Create_an_deal_in_Pipedrive.json](workflows/113_Create_an_deal_in_Pipedrive.json) |
| Create a customer and add them to a segment in Customer.io | create_contact | customerio, manual | 🟢 Low | [32_Create_a_customer_and_add_them_to_a_segment_in_Customer.io.json](workflows/32_Create_a_customer_and_add_them_to_a_segment_in_Customer.io.json) |
| Create a new contact in Agile CRM | create_contact | agilecrm, manual | 🟢 Low | [96_Create_a_new_contact_in_Agile_CRM.json](workflows/96_Create_a_new_contact_in_Agile_CRM.json) |
| Create a new customer in Chargebee | create_contact | chargebee, manual | 🟢 Low | [103_Create_a_new_customer_in_Chargebee.json](workflows/103_Create_a_new_customer_in_Chargebee.json) |
| Receive updates when a customer is created in HelpScout | create_contact | helpscout | 🟢 Low | [61_Receive_updates_when_a_customer_is_created_in_HelpScout.json](workflows/61_Receive_updates_when_a_customer_is_created_in_HelpScout.json) |
| Create a QuickBooks invoice on a new Onfleet Task creation | create_task | onfleet, quickbooks | 🟢 Low | [1546_Create_a_QuickBooks_invoice_on_a_new_Onfleet_Task_creation.json](workflows/1546_Create_a_QuickBooks_invoice_on_a_new_Onfleet_Task_creation.json) |
| Generate Leads with Google Maps - AlexK1919 | generate | splitinbatches, httprequest, stopanderror | 🔴 High | [cQAILffOajE9n2cf_Generate_Leads_with_Google_Maps_-_AlexK1919.json](workflows/cQAILffOajE9n2cf_Generate_Leads_with_Google_Maps_-_AlexK1919.json) |
| Convert Squarespace Profiles to Shopify Customers in Google Sheets | process | splitinbatches, webhook, manual | 🟡 Medium | [7Gw4IfHaVMDSj70o_Convert_Squarespace_Profiles_to_Shopify_Customers_in_Google_Sheets.json](workflows/7Gw4IfHaVMDSj70o_Convert_Squarespace_Profiles_to_Shopify_Customers_in_Google_Sheets.json) |
| Get information about a company with UpLead | read | uplead, manual | 🟢 Low | [129_Get_information_about_a_company_with_UpLead.json](workflows/129_Get_information_about_a_company_with_UpLead.json) |
| Stripe Payment Order Sync – Auto Retrieve Customer & Product Purchased | sync | stripe, httprequest | 🟢 Low | [YVNJOltj0jMQatGz_Stripe_Payment_Order_Sync_–_Auto_Retrieve_Customer_&_Product_Purchased.json](workflows/YVNJOltj0jMQatGz_Stripe_Payment_Order_Sync_–_Auto_Retrieve_Customer_&_Product_Purchased.json) |
| Sync New Shopify Customers to Odoo Contacts | sync | odoo, shopify | 🟢 Low | [Zp0R3I1dUjZOIz2l_Sync_New_Shopify_Customers_to_Odoo_Contacts.json](workflows/Zp0R3I1dUjZOIz2l_Sync_New_Shopify_Customers_to_Odoo_Contacts.json) |
| Two Way Sync Pipedrive and MySQL | sync | pipedrive, datetime, comparedatasets | 🔴 High | [65_Two_Way_Sync_Pipedrive_and_MySQL.json](workflows/65_Two_Way_Sync_Pipedrive_and_MySQL.json) |
| Receive updates for all changes in Pipedrive | update | pipedrive | 🟢 Low | [115_Receive_updates_for_all_changes_in_Pipedrive.json](workflows/115_Receive_updates_for_all_changes_in_Pipedrive.json) |
| Receive updates for events in Chargebee | update | chargebee | 🟢 Low | [108_Receive_updates_for_events_in_Chargebee.json](workflows/108_Receive_updates_for_events_in_Chargebee.json) |
| Receive updates when a billing plan is activated in PayPal | update | paypal | 🟢 Low | [46_Receive_updates_when_a_billing_plan_is_activated_in_PayPal.json](workflows/46_Receive_updates_when_a_billing_plan_is_activated_in_PayPal.json) |
| Receive updates when a subscriber unsubscribes in Customer.io | update | customerio | 🟢 Low | [29_Receive_updates_when_a_subscriber_unsubscribes_in_Customer.io.json](workflows/29_Receive_updates_when_a_subscriber_unsubscribes_in_Customer.io.json) |

## CONTENT

*37 workflows in this category*

| Workflow Name | Business Function | Key Integrations | Complexity | File |
|---------------|-------------------|------------------|------------|------|
|  | automate | contentful, manual | 🟢 Low | [640_.json](workflows/640_.json) |
| (Not published) Three-View Orthographic Projection to Dynamic Video Conversion | automate | httprequest, manual | 🟡 Medium | [KWFLpcJytH7qjheD_(Not_published)_Three-View_Orthographic_Projection_to_Dynamic_Video_Conversion.json](workflows/KWFLpcJytH7qjheD_(Not_published)_Three-View_Orthographic_Projection_to_Dynamic_Video_Conversion.json) |
| 1130_workflow_1130 | automate | twitter, manual | 🟢 Low | [1130_workflow_1130.json](workflows/1130_workflow_1130.json) |
| 1376_workflow_1376 | automate | twitter, httprequest, cron | 🟢 Low | [1376_workflow_1376.json](workflows/1376_workflow_1376.json) |
| 1535_workflow_1535 | automate | googlecloudnaturallanguage, interval, webhook | 🔴 High | [1535_workflow_1535.json](workflows/1535_workflow_1535.json) |
| 2211_workflow_2211 | automate | manual, youtube | 🟡 Medium | [2211_workflow_2211.json](workflows/2211_workflow_2211.json) |
| 2518_workflow_2518 | automate | splitinbatches, comparedatasets, spotify | 🟡 Medium | [2518_workflow_2518.json](workflows/2518_workflow_2518.json) |
| 2889_workflow_2889 | automate | wordpress, manual, googledrive | 🟡 Medium | [2889_workflow_2889.json](workflows/2889_workflow_2889.json) |
| 3216_workflow_3216 | automate | emailsend, httprequest, rssfeedread | 🔴 High | [3216_workflow_3216.json](workflows/3216_workflow_3216.json) |
| 3786_workflow_3786 | automate | facebookleadads | 🟢 Low | [3786_workflow_3786.json](workflows/3786_workflow_3786.json) |
| 514_workflow_514 | automate | manual, facebookgraphapi | 🟢 Low | [514_workflow_514.json](workflows/514_workflow_514.json) |
| 546_workflow_546 | automate | wordpress, manual | 🟢 Low | [546_workflow_546.json](workflows/546_workflow_546.json) |
| 681_workflow_681 | automate | httprequest, manual, linkedin | 🟢 Low | [681_workflow_681.json](workflows/681_workflow_681.json) |
| Automate testimonials in Strapi with n8n | automate | googlecloudnaturallanguage, interval, webhook | 🔴 High | [Automate testimonials in Strapi with n8n.json](workflows/Automate testimonials in Strapi with n8n.json) |
| Fully automated Video Captions generation with json2video | automate | httprequest, manual | 🟡 Medium | [Tygtx1aZi9pLdtUo_Fully_automated_Video_Captions_generation_with_json2video.json](workflows/Tygtx1aZi9pLdtUo_Fully_automated_Video_Captions_generation_with_json2video.json) |
| Post on X | automate | airtop, executeworkflow, form | 🟡 Medium | [plzObaqgoEvV4UU0_Post_on_X.json](workflows/plzObaqgoEvV4UU0_Post_on_X.json) |
| Publish Image Post to Bluesky | automate | httprequest, manual | 🔴 High | [XGFs5jZNCeURd4OT_Publish_Image_Post_to_Bluesky.json](workflows/XGFs5jZNCeURd4OT_Publish_Image_Post_to_Bluesky.json) |
| Publish post to a publication | automate | medium, manual | 🟢 Low | [7_Publish_post_to_a_publication.json](workflows/7_Publish_post_to_a_publication.json) |
| Social Media Publisher | automate | httprequest, form, form | 🔴 High | [r1u4HOJu5j5sP27x_Social_Media_Publisher.json](workflows/r1u4HOJu5j5sP27x_Social_Media_Publisher.json) |
| Turn YouTube Videos into Summaries, Transcripts, and Visual Insights | automate | httprequest, manual | 🔴 High | [wZBgoWrBZveMmzYi_Turn_YouTube_Videos_into_Summaries,_Transcripts,_and_Visual_Insights.json](workflows/wZBgoWrBZveMmzYi_Turn_YouTube_Videos_into_Summaries,_Transcripts,_and_Visual_Insights.json) |
| TwitterWorkflow | automate | rocketchat, manual, cron | 🟡 Medium | [1_TwitterWorkflow.json](workflows/1_TwitterWorkflow.json) |
| Upload video to drive via google script | automate | httprequest, manual, googledrive | 🟢 Low | [wGv0NPBA0QLp4rQ6_Upload_video_to_drive_via_google_script.json](workflows/wGv0NPBA0QLp4rQ6_Upload_video_to_drive_via_google_script.json) |
| Wordpress-to-csv | automate | spreadsheetfile, writebinaryfile, wordpress | 🟢 Low | [1_Wordpress-to-csv.json](workflows/1_Wordpress-to-csv.json) |
| post to mattermost v2 | automate | httprequest, rssfeedread, cron | 🟡 Medium | [2_post_to_mattermost_v2.json](workflows/2_post_to_mattermost_v2.json) |
| post to wallabag | automate | httprequest, manual, cron | 🟡 Medium | [4_post_to_wallabag.json](workflows/4_post_to_wallabag.json) |
| upload-post images | automate | httprequest, manual | 🟡 Medium | [ra8MrqshnzXPy55O_upload-post_images.json](workflows/ra8MrqshnzXPy55O_upload-post_images.json) |
| Automatically Update YouTube Video Descriptions with Inserted Text | create | splitinbatches, manual, youtube | 🟡 Medium | [3080_Automatically_Update_YouTube_Video_Descriptions_with_Inserted_Text.json](workflows/3080_Automatically_Update_YouTube_Video_Descriptions_with_Inserted_Text.json) |
| Create a new member, update the information of the member, create a note and a post for the member in Orbit | create | orbit, manual | 🟢 Low | [105_Create_a_new_member,_update_the_information_of_the_member,_create_a_note_and_a_post_for_the_member_in_Orbit.json](workflows/105_Create_a_new_member,_update_the_information_of_the_member,_create_a_note_and_a_post_for_the_member_in_Orbit.json) |
| Create a post and update the post in WordPress | create | wordpress, manual | 🟢 Low | [60_Create_a_post_and_update_the_post_in_WordPress.json](workflows/60_Create_a_post_and_update_the_post_in_WordPress.json) |
| Create, update, and get a post in Ghost | create | ghost, manual | 🟢 Low | [170_Create,_update,_and_get_a_post_in_Ghost.json](workflows/170_Create,_update,_and_get_a_post_in_Ghost.json) |
| Create, update, and get an entry in Strapi | create | manual, strapi | 🟢 Low | [119_Create,_update,_and_get_an_entry_in_Strapi.json](workflows/119_Create,_update,_and_get_an_entry_in_Strapi.json) |
| Receive updates when a new activity gets created and tweet about it | create | strava, twitter | 🟢 Low | [95_Receive_updates_when_a_new_activity_gets_created_and_tweet_about_it.json](workflows/95_Receive_updates_when_a_new_activity_gets_created_and_tweet_about_it.json) |
| Upload video, create playlist and add video to playlist | create | manual, readbinaryfile, youtube | 🟢 Low | [21_Upload_video,_create_playlist_and_add_video_to_playlist.json](workflows/21_Upload_video,_create_playlist_and_add_video_to_playlist.json) |
| Youtube Video Transcript Extraction | extract | httprequest, form | 🟢 Low | [XxkmcgZC4OtIOVoD_Youtube_Video_Transcript_Extraction.json](workflows/XxkmcgZC4OtIOVoD_Youtube_Video_Transcript_Extraction.json) |
| Generate 360° Virtual Try-on Videos for Clothing with Kling API | generate | httprequest, manual | 🔴 High | [xQ0xqhNzFeEdBpFK_Generate_360°_Virtual_Try-on_Videos_for_Clothing_with_Kling_API.json](workflows/xQ0xqhNzFeEdBpFK_Generate_360°_Virtual_Try-on_Videos_for_Clothing_with_Kling_API.json) |
| Get Comments from Facebook Page | read | manual, facebookgraphapi | 🟡 Medium | [5DiXT9FykJvuElc1_Get_Comments_from_Facebook_Page.json](workflows/5DiXT9FykJvuElc1_Get_Comments_from_Facebook_Page.json) |
| Automated Content SEO Audit Report | report | splitinbatches, httprequest, manual | 🔴 High | [Tqa8dikBDLYEytx5_Automated_Content_SEO_Audit_Report.json](workflows/Tqa8dikBDLYEytx5_Automated_Content_SEO_Audit_Report.json) |

## OPS

*34 workflows in this category*

| Workflow Name | Business Function | Key Integrations | Complexity | File |
|---------------|-------------------|------------------|------------|------|
| 1132_workflow_1132 | automate | github, travisci | 🟢 Low | [1132_workflow_1132.json](workflows/1132_workflow_1132.json) |
| 1222_workflow_1222 | automate | httprequest, github, cron | 🟡 Medium | [1222_workflow_1222.json](workflows/1222_workflow_1222.json) |
| 1274_workflow_1274 | automate | github, github | 🟡 Medium | [1274_workflow_1274.json](workflows/1274_workflow_1274.json) |
| 1349_workflow_1349 | automate | gitlab, github, cron | 🟡 Medium | [1349_workflow_1349.json](workflows/1349_workflow_1349.json) |
| 1375_workflow_1375 | automate | httprequest, gitlab | 🟢 Low | [1375_workflow_1375.json](workflows/1375_workflow_1375.json) |
| 1832_workflow_1832 | automate | webhook, github, zendesk | 🟡 Medium | [1832_workflow_1832.json](workflows/1832_workflow_1832.json) |
| 1856_workflow_1856 | automate | homeassistant, github | 🟢 Low | [1856_workflow_1856.json](workflows/1856_workflow_1856.json) |
| 2307_workflow_2307 | automate | splitinbatches, httprequest, executecommand | 🔴 High | [2307_workflow_2307.json](workflows/2307_workflow_2307.json) |
| 2376_workflow_2376 | automate | gitlab, schedule, manual | 🔴 High | [2376_workflow_2376.json](workflows/2376_workflow_2376.json) |
| 2385_workflow_2385 | automate | splitinbatches, gitlab, manual | 🔴 High | [2385_workflow_2385.json](workflows/2385_workflow_2385.json) |
| 2652_workflow_2652 | automate | splitinbatches, httprequest, schedule | 🔴 High | [2652_workflow_2652.json](workflows/2652_workflow_2652.json) |
| 2868_workflow_2868 | automate | splitinbatches, httprequest, schedule | 🔴 High | [2868_workflow_2868.json](workflows/2868_workflow_2868.json) |
| 3635_workflow_3635 | automate | httprequest, n8n-nodes-langchain.mcp, n8n-nodes-langchain.workflow | 🔴 High | [3635_workflow_3635.json](workflows/3635_workflow_3635.json) |
| 527_workflow_527 | automate | github | 🟢 Low | [527_workflow_527.json](workflows/527_workflow_527.json) |
| 528_workflow_528 | automate | gitlab | 🟢 Low | [528_workflow_528.json](workflows/528_workflow_528.json) |
| 817_workflow_817 | automate | splitinbatches, httprequest, manual | 🔴 High | [817_workflow_817.json](workflows/817_workflow_817.json) |
| Automate assigning GitHub issues | automate | github, github | 🟡 Medium | [122_Automate_assigning_GitHub_issues.json](workflows/122_Automate_assigning_GitHub_issues.json) |
| PUQ Docker NextCloud deploy | automate | ssh, httprequest, webhook | 🔴 High | [d3xtaER6gl4aqLZR_PUQ_Docker_NextCloud_deploy.json](workflows/d3xtaER6gl4aqLZR_PUQ_Docker_NextCloud_deploy.json) |
| Restore your credentials from GitHub | automate | httprequest, manual, github | 🟡 Medium | [7zRCNv7B5WFRg7ux_Restore_your_credentials_from_GitHub.json](workflows/7zRCNv7B5WFRg7ux_Restore_your_credentials_from_GitHub.json) |
| Restore your workflows from GitHub | automate | httprequest, manual, github | 🟡 Medium | [XYz1JYUXFHFVdlLj_Restore_your_workflows_from_GitHub.json](workflows/XYz1JYUXFHFVdlLj_Restore_your_workflows_from_GitHub.json) |
| Trigger a build using the TravisCI node | automate | manual, travisci | 🟢 Low | [52_Trigger_a_build_using_the_TravisCI_node.json](workflows/52_Trigger_a_build_using_the_TravisCI_node.json) |
| [OPS] Restore workflows from GitHub to n8n | automate | manual, github, n8n | 🔴 High | [uoBZx3eMvLMxlHCS_[OPS]_Restore_workflows_from_GitHub_to_n8n.json](workflows/uoBZx3eMvLMxlHCS_[OPS]_Restore_workflows_from_GitHub_to_n8n.json) |
| [n8n] Advanced URL Parsing and Shortening Workflow - Switchy.io Integration | automate | splitinbatches, respondtowebhook, httprequest | 🔴 High | [2064_[n8n]_Advanced_URL_Parsing_and_Shortening_Workflow_-_Switchy.io_Integration.json](workflows/2064_[n8n]_Advanced_URL_Parsing_and_Shortening_Workflow_-_Switchy.io_Integration.json) |
| n8n workflow deployer | automate | httprequest, manual, extractfromfile | 🔴 High | [bhWsUxipJ9wuTA5K_n8n_workflow_deployer.json](workflows/bhWsUxipJ9wuTA5K_n8n_workflow_deployer.json) |
| new | automate | manual, github | 🟢 Low | [5_new.json](workflows/5_new.json) |
| puq-docker-immich-deploy | automate | ssh, webhook, respondtowebhook | 🔴 High | [qps97Q4NEet1Pkm4_puq-docker-immich-deploy.json](workflows/qps97Q4NEet1Pkm4_puq-docker-immich-deploy.json) |
| puq-docker-influxdb-deploy | automate | ssh, webhook, respondtowebhook | 🔴 High | [bpq5aoogWibWq94t_puq-docker-influxdb-deploy.json](workflows/bpq5aoogWibWq94t_puq-docker-influxdb-deploy.json) |
| puq-docker-minio-deploy | automate | ssh, webhook, respondtowebhook | 🔴 High | [IJYpB2CIAdLk8Umg_puq-docker-minio-deploy.json](workflows/IJYpB2CIAdLk8Umg_puq-docker-minio-deploy.json) |
| puq-docker-n8n-deploy | automate | ssh, webhook, respondtowebhook | 🔴 High | [cY8OVKzHS0ScRhP9_puq-docker-n8n-deploy.json](workflows/cY8OVKzHS0ScRhP9_puq-docker-n8n-deploy.json) |
| Backup Squarespace code Injections to Github | backup | splitinbatches, httprequest, schedule | 🔴 High | [eB4rTdZFvrdKK5VP_Backup_Squarespace_code_Injections_to_Github.json](workflows/eB4rTdZFvrdKK5VP_Backup_Squarespace_code_Injections_to_Github.json) |
| Backup workflows to git repository | backup | splitinbatches, schedule, github | 🔴 High | [2532_Backup_workflows_to_git_repository.json](workflows/2532_Backup_workflows_to_git_repository.json) |
| Clockify Backup Template | backup | httprequest, stopanderror, comparedatasets | 🔴 High | [k22TSNIZXHaQ9rGr_Clockify_Backup_Template.json](workflows/k22TSNIZXHaQ9rGr_Clockify_Backup_Template.json) |
| Remote IOT Sensor monitoring via MQTT and InfluxDB | monitor | mqtt, httprequest | 🟢 Low | [6pOGYw5O3iOY1Gc6_Remote_IOT_Sensor_monitoring_via_MQTT_and_InfluxDB.json](workflows/6pOGYw5O3iOY1Gc6_Remote_IOT_Sensor_monitoring_via_MQTT_and_InfluxDB.json) |
| Dashboard | report | httprequest, github, cron | 🔴 High | [6_Dashboard.json](workflows/6_Dashboard.json) |

## ECOMMERCE

*13 workflows in this category*

| Workflow Name | Business Function | Key Integrations | Complexity | File |
|---------------|-------------------|------------------|------------|------|
| 1808_workflow_1808 | automate | shopify, zendesk | 🟡 Medium | [1808_workflow_1808.json](workflows/1808_workflow_1808.json) |
| 1809_workflow_1809 | automate | zendesk, shopify | 🟡 Medium | [1809_workflow_1809.json](workflows/1809_workflow_1809.json) |
| 1829_workflow_1829 | automate | mautic, shopify | 🟢 Low | [1829_workflow_1829.json](workflows/1829_workflow_1829.json) |
| 3296_workflow_3296 | automate | splitinbatches, shopify, httprequest | 🔴 High | [3296_workflow_3296.json](workflows/3296_workflow_3296.json) |
| 547_workflow_547 | automate | shopify | 🟢 Low | [547_workflow_547.json](workflows/547_workflow_547.json) |
| 548_workflow_548 | automate | manual, shopify | 🟢 Low | [548_workflow_548.json](workflows/548_workflow_548.json) |
| Creating an Onfleet Task for a new Shopify Fulfillment | automate | onfleet, shopify | 🟢 Low | [13_Creating_an_Onfleet_Task_for_a_new_Shopify_Fulfillment.json](workflows/13_Creating_an_Onfleet_Task_for_a_new_Shopify_Fulfillment.json) |
| Shopify + Mautic | automate | crypto, mautic, graphql | 🔴 High | [JiSesGjDIXIPYtbt_Shopify_+_Mautic.json](workflows/JiSesGjDIXIPYtbt_Shopify_+_Mautic.json) |
| Shopify order UTM to Baserow | automate | graphql, schedule, baserow | 🟡 Medium | [ZI0PxugfKsyepqeH_Shopify_order_UTM_to_Baserow.json](workflows/ZI0PxugfKsyepqeH_Shopify_order_UTM_to_Baserow.json) |
| Updating Shopify tags on Onfleet events | automate | onfleet, shopify | 🟢 Low | [1545_Updating_Shopify_tags_on_Onfleet_events.json](workflows/1545_Updating_Shopify_tags_on_Onfleet_events.json) |
| Create, update and get a product from WooCommerce | create | woocommerce, manual | 🟢 Low | [187_Create,_update_and_get_a_product_from_WooCommerce.json](workflows/187_Create,_update_and_get_a_product_from_WooCommerce.json) |
| Create, update, and get a document in Google Cloud Firestore | create | manual, googlefirebasecloudfirestore | 🟢 Low | [179_Create,_update,_and_get_a_document_in_Google_Cloud_Firestore.json](workflows/179_Create,_update,_and_get_a_document_in_Google_Cloud_Firestore.json) |
| Import Odoo Product Images from Google Drive | transfer | schedule, googlechat, manual | 🔴 High | [4aKofiCShqdDSsIS_Import_Odoo_Product_Images_from_Google_Drive.json](workflows/4aKofiCShqdDSsIS_Import_Odoo_Product_Images_from_Google_Drive.json) |

## ANALYTICS

*12 workflows in this category*

| Workflow Name | Business Function | Key Integrations | Complexity | File |
|---------------|-------------------|------------------|------------|------|
| Google analytics template | automate | googleanalytics, httprequest, schedule | 🔴 High | [K3uf8aY8wipScEay_Google_analytics_template.json](workflows/K3uf8aY8wipScEay_Google_analytics_template.json) |
| Google analytics template | automate | googleanalytics, httprequest, schedule | 🔴 High | [Send Google analytics data to A.I. to analyze then save results in Baserow.json](workflows/Send Google analytics data to A.I. to analyze then save results in Baserow.json) |
| Google analytics template | automate | googleanalytics, httprequest, schedule | 🔴 High | [Send Google analytics data to A.I. to analyze then save results in BaserowSend Google analytics data to A.I. to analyze then save results in Baserow.json](workflows/Send Google analytics data to A.I. to analyze then save results in BaserowSend Google analytics data to A.I. to analyze then save results in Baserow.json) |
| SERPBear analytics template | automate | httprequest, schedule, baserow | 🟡 Medium | [qmmXKcpJOCm9qaCk_SERPBear_analytics_template.json](workflows/qmmXKcpJOCm9qaCk_SERPBear_analytics_template.json) |
| SERPBear analytics template | automate | httprequest, schedule, baserow | 🟡 Medium | [Summarize SERPBear data with AI (via Openrouter) and save it to Baserow.json](workflows/Summarize SERPBear data with AI (via Openrouter) and save it to Baserow.json) |
| Umami analytics template | automate | httprequest, schedule, baserow | 🔴 High | [eZT6SZ4Kvmq5TzyQ_Umami_analytics_template.json](workflows/eZT6SZ4Kvmq5TzyQ_Umami_analytics_template.json) |
| Umami analytics template | automate | httprequest, schedule, baserow | 🔴 High | [Summarize Umami data with AI (via Openrouter) and save it to Baserow.json](workflows/Summarize Umami data with AI (via Openrouter) and save it to Baserow.json) |
| Track an event in Segment | monitor | segment, manual | 🟢 Low | [122_Track_an_event_in_Segment.json](workflows/122_Track_an_event_in_Segment.json) |
| Matomo Analytics Report | report | httprequest, schedule, baserow | 🟡 Medium | [PRQhetYFkuhxntVH_Matomo_Analytics_Report.json](workflows/PRQhetYFkuhxntVH_Matomo_Analytics_Report.json) |
| Steam + CF Report | report | webhook, mailgun, executecommand | 🟡 Medium | [122_Steam_+_CF_Report.json](workflows/122_Steam_+_CF_Report.json) |
| Weekly_Shodan_Query___Report_Accidents__no_function_node_ | report | splitinbatches, itemlists, httprequest | 🔴 High | [VoLT6Omw9KMQgPum_Weekly_Shodan_Query___Report_Accidents__no_function_node_.json](workflows/VoLT6Omw9KMQgPum_Weekly_Shodan_Query___Report_Accidents__no_function_node_.json) |
| n8n Error Report to Line | report | error, httprequest | 🟢 Low | [ePnGZtZ8zLcf1UZZ_n8n_Error_Report_to_Line.json](workflows/ePnGZtZ8zLcf1UZZ_n8n_Error_Report_to_Line.json) |

## MARKETING

*1 workflows in this category*

| Workflow Name | Business Function | Key Integrations | Complexity | File |
|---------------|-------------------|------------------|------------|------|
|  | automate | activecampaign, manual | 🟢 Low | [412_.json](workflows/412_.json) |

---

## 🛠️ Usage Instructions

1. **Browse by Category**: Use the navigation links above to jump to specific workflow categories
2. **Find by Integration**: Use Ctrl+F to search for specific service integrations
3. **Check Complexity**: Look at complexity badges to assess implementation difficulty
4. **Download Workflows**: Click on workflow file links to view the JSON configuration

## 📝 Contributing

To add new workflows to this collection:
1. Add your workflow JSON file to the `workflows/` directory
2. Follow the naming convention: `{category}_{function}_{description}_{integrations}.json`
3. Run the analysis script to update this documentation

## 🔧 Technical Details

- **Total Workflow Files**: 2,050
- **Analysis Errors**: 0
- **Generated**: Automatically generated from workflow analysis
