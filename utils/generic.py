# from database.dao.dao import TicketDAO

# def generic_type(ticket_type: list):
#     tickets = TicketDAO.find_all_or_none(ticket_type=ticket_type)
#     tickets_dict = dict()
#     for ticket in tickets:
#         text = 'meow'
#         tickets_dict[ticket.model.username] = text
#     return tickets_dict

#
# f'Тип проблемы: {ticket.get('ticket_type')}\n'
            #    f'Имя пользователя:{ticket.get('username')}\n'
            #    f'Текст проблемы:\n{ticket.get('ticket_text')}