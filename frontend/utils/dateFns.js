import { format, formatDistanceToNow, isThisYear } from "date-fns";

export const formatDate = (date) => {
  const now = new Date();
  const timeAgo = formatDistanceToNow(date, { addSuffix: true });

  if (!isThisYear(date)) {
    // For past years, show "Aug 24, 2020"
    return format(date, "MMM d, yyyy");
  } else if (now - date > 7 * 24 * 60 * 60 * 1000) {
    // For dates older than 7 days but in the same year, show "Aug 24"
    return format(date, "MMM d");
  } else {
    // For less than 7 days, show relative time like "5 hours ago"
    return timeAgo;
  }
};
