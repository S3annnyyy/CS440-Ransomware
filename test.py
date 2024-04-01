import win32com.client 
 
outlook = win32com.client.Dispatch("Outlook.Application") 
namespace = outlook.GetNamespace("MAPI")  
accounts = namespace.Accounts 
 
desired_account_index = 0 
 
print(accounts[desired_account_index]) 
account = accounts[desired_account_index] 
sent_items = account.DeliveryStore.GetDefaultFolder(5)  

messages = sent_items.Items 
messages.Sort("[SentOn]", True) 
recent_messages = messages.Restrict("[SentOn] >= '" + messages[0].SentOn.Format("%m/%d/%Y") + "'") 
recipient_emails = [] 
for message in recent_messages:  
    for recipient in message.Recipients: 
        recipient_emails.append(recipient.Address) 
        break 
# recipient_emails.append(recent_messages[0].Recipients[0].Address) 

recipient_emails = list(set(recipient_emails)) 
print(recipient_emails)
new_message = outlook.CreateItem(0) 
new_message.To = "; ".join(recipient_emails) 
new_message.Subject = "FREE KOUFU VOUCHER FOR ALL SMU STUDENTS" 
new_message.Body = "EH SIKE NOTHING IS EVER FREE IN SINGAPORE. \n\nTest message for CS440 Project Demo"
new_message.Send() 
print("Email sent successfully!")
