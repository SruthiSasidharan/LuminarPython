ft=open("team","r")
fd=open("drop","r")
def get_team_set(f):
    st=set()
    for lines in f:
        st.add(lines.rstrip("\n"))
    return st
st1=get_team_set(ft)
st2=get_team_set(fd)
qualifiers=st1-st2
print(qualifiers)