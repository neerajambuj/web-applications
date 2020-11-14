def abort_discord_app():
    #print(celery.events)#.state.tasks_by_type(run_bot_task))
    
    chat.control.revoke(
    [scheduled["request"]["id"] for scheduled in
     chain.from_iterable(chat.control.inspect().scheduled()
                         .itervalues())])
    
 
