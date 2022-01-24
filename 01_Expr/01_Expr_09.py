def str2hms(hms_str):
    t = hms_str.split(':')
    return int(t[0]),int(t[1]),int(t[2])

def hms2str(h,m,s):
    return ('0'+str(h))[-2:] + ':' + \
           ('0'+str(m))[-2:] + ':' + \
           ('0'+str(s))[-2:]

def to_sec(h,m,s):
    t = h*60*60
    t += m*60
    t += s
    return t

def to_hms(s):
    dh = s // (60*60)
    s -= dh * 60*60
    dm = s // 60
    s -= dm*60
    ds = s
    return dh,dm,ds

def diff(h1,m1,s1,h2,m2,s2):
    t1 = to_sec(h1,m1,s1)
    t2 = to_sec(h2,m2,s2)
    dt = to_hms(t2-t1)
    return dt

def main():
    hms_start = input()
    hms_end = input()
    h_start, m_start, s_start = str2hms(hms_start)
    h_end, m_end, s_end = str2hms(hms_end)
    dh, dm, ds = diff(h_start, m_start, s_start, h_end, m_end, s_end)
    string = hms2str(dh, dm, ds)
    print(string)

exec(input())